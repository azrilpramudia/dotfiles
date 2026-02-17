import datetime
from email.policy import default
import json
import subprocess
from collections import defaultdict
from kitty.boss import get_boss
from kitty.fast_data_types import Screen, add_timer
from kitty.tab_bar import (
    DrawData,
    ExtraData,
    Formatter,
    TabBarData,
    as_rgb,
    draw_attributed_string,
    draw_tab_with_powerline,
)

timer_id = None

def draw_tab(
    draw_data: DrawData,
    screen: Screen,
    tab: TabBarData,
    before: int,
    max_title_length: int,
    index: int,
    is_last: bool,
    extra_data: ExtraData,
) -> int:
    global timer_id
    if timer_id is None:
        timer_id = add_timer(_redraw_tab_bar, 0.1, True)

    tab = tab._replace(title=f"{index}")
    
    screen.cursor.bold = True
    draw_tab_with_powerline(
        draw_data, screen, tab, before, max_title_length, index, is_last, extra_data
    )
    screen.cursor.bold = False
    
    if is_last:
        draw_right_status(draw_data, screen)
    
    return screen.cursor.x

def draw_right_status(draw_data: DrawData, screen: Screen) -> None:
    draw_attributed_string(Formatter.reset, screen)
    
    cells = create_cells()
    if not cells:
        return
    
    while True:
        padding = screen.columns - screen.cursor.x - sum(len(c) + 3 for c in cells)
        if padding >= 0:
            break
        if not cells:
            return
        cells = cells[1:]

    if padding > 0:
        screen.draw(" " * padding)

    cell_colors = [
        (as_rgb(0x61AFEF), as_rgb(0x282C34)), 
        (as_rgb(0xC678DD), as_rgb(0x282C34)),
        (as_rgb(0x98C379), as_rgb(0x282C34)),
    ]
    
    default_bg = as_rgb(int(draw_data.default_bg))

    for i, cell in enumerate(cells):
        current_bg, current_fg = cell_colors[i] if i < len(cell_colors) else cell_colors[-1]

        # --- SEPARATOR --- #
        if i == 0:
            screen.cursor.fg = current_bg
            screen.cursor.bg = default_bg
            screen.draw("")
        else:
            prev_bg = cell_colors[i-1][0]
            screen.cursor.fg = current_bg
            screen.cursor.bg = prev_bg
            screen.draw("")

        # --- CELLS --- #
        screen.cursor.bold = True    
        screen.cursor.fg = current_fg
        screen.cursor.bg = current_bg
        screen.draw(f" {cell} ")
        screen.cursor.bold = False

def create_cells() -> list:
    """Create status cells - Spotify + Time"""
    cells = []
    
    # Spotify Status
    song = get_spotify_status()
    if song:
        cells.append(song)
    
    # Date and time
    now = datetime.datetime.now()
    cells.append(now.strftime("%d %b"))
    cells.append(now.strftime("%I:%M"))
    
    return cells

def _redraw_tab_bar(timer_id):
    from kitty.boss import get_boss
    boss = get_boss()
    if boss:
        boss.set_colors()

# ================= Spotify =================
import time

def get_spotify_status():
    try:
        raw = subprocess.getoutput(
            "playerctl metadata --format '{{status}} {{artist}} - {{title}}' 2>/dev/null"
        ).strip()
        
        if not raw or "No players found" in raw:
            return None

        # Split the status and metadata
        parts = raw.split(" ", 1)
        play_status = parts[0]
        metadata = parts[1] if len(parts) > 1 else "Spotify"

        status_icon = "󰐊" if play_status == "Playing" else "󰏤"
        music_icon = "󰝚"

        display_len = 20
        if len(metadata) > display_len:
            padding_text = metadata + "   |   "
            # Only scroll if the song is playing
            speed = 2 if play_status == "Playing" else 0 
            shift = int(time.time() * speed) % len(padding_text) if speed > 0 else 0
            metadata = (padding_text[shift:] + padding_text[:shift])[:display_len]
            
        return f"{music_icon} {status_icon} {metadata}"
    except Exception:
        return None