import datetime
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
    # if timer_id is None:
    #     timer_id = add_timer(_redraw_tab_bar, 2.0, True)
    
    draw_tab_with_powerline(
        draw_data, screen, tab, before, max_title_length, index, is_last, extra_data
    )
    
    if is_last:
        draw_right_status(draw_data, screen)
    
    return screen.cursor.x

def draw_right_status(draw_data: DrawData, screen: Screen) -> None:
    """Draw right status dengan powerline separator"""
    draw_attributed_string(Formatter.reset, screen)
    
    cells = create_cells()
    if not cells:
        return
    
    # Colors
    default_bg = as_rgb(int(draw_data.default_bg))
    
    cell_colors = [
        (0x61AFEF, 0x282C34),
        (0x98C379, 0x282C34),  
        (0xE5C07B, 0x282C34),  
    ]
    
    # Hitung total width untuk semua cells dengan separator
    total_width = 0
    for i, cell in enumerate(cells):
        cell_text = str(cell[1]) if isinstance(cell, tuple) else str(cell)
        
        # Hitung lebar cell + icon adjustment
        cell_width = len(cell_text) + 2  # +2 untuk space kiri-kanan " text "
        if '' in cell_text:
            cell_width += 1  # icon butuh extra space
        
        total_width += cell_width  # untuk separator ""
    total_width += 0  # +1 untuk separator kanan ""
    
    # Posisi start dari kanan
    right_pos = screen.columns - total_width
    if right_pos < screen.cursor.x:
        right_pos = screen.cursor.x
    
    screen.cursor.x = right_pos
    
    # Draw cells dengan powerline separator
    for i, cell in enumerate(cells):
        cell_text = str(cell[1]) if isinstance(cell, tuple) else str(cell)
        
        # Ambil warna cell
        if i < len(cell_colors):
            cell_bg, cell_fg = cell_colors[i]
            cell_bg = as_rgb(cell_bg)
            cell_fg = as_rgb(cell_fg)
        else:
            cell_bg = as_rgb(int(draw_data.active_bg))
            cell_fg = as_rgb(int(draw_data.active_fg))
        
        # Draw separator powerline "" (kiri - arah kanan)
        if i == 0:
            screen.cursor.fg = cell_bg
            screen.cursor.bg = default_bg
        else:
            prev_bg = as_rgb(cell_colors[i-1][0]) if i-1 < len(cell_colors) else cell_bg
            screen.cursor.fg = cell_bg
            screen.cursor.bg = prev_bg
        
        screen.draw("")  # Powerline classic kiri
        
        # Draw cell content
        screen.cursor.fg = cell_fg
        screen.cursor.bg = cell_bg
        screen.draw(f" {cell_text} ")

def create_cells() -> list:
    """Create status cells - tanpa battery"""
    cells = []
    
    # Git branch
    git = get_git_branch()
    if git:
        cells.append(git)
    
    # Date and time
    now = datetime.datetime.now()
    cells.append(now.strftime("%d %b"))
    cells.append(now.strftime("%I:%M %p"))
    
    return cells


# ================= GIT BRANCH =================
def get_git_branch():
    try:
        boss = get_boss()
        window = boss.active_window
        if not window:
            return " ~"

        pid = window.child.pid
        cwd = subprocess.getoutput(f"readlink -f /proc/{pid}/cwd")

        if not cwd:
            return " ~"

        is_repo = subprocess.getoutput(
            f"git -C '{cwd}' rev-parse --is-inside-work-tree 2>/dev/null"
        )

        if is_repo.strip() != "true":
            return " ~"

        branch = subprocess.getoutput(
            f"git -C '{cwd}' rev-parse --abbrev-ref HEAD 2>/dev/null"
        )

        return f" {branch}"
    except Exception:
        return " ~"


# ================= OPTIONAL: Keep original functions =================
def get_headphone_battery_status():
    """Original headphone battery from community config"""
    try:
        battery_pct = int(subprocess.getoutput("headsetcontrol -b -c"))
    except Exception:
        status = ""
    else:
        if battery_pct < 0:
            status = ""
        else:
            status = f"{battery_pct}% {''[battery_pct // 10]}"
    return f" {status}"


STATE = defaultdict(lambda: "", {"Paused": "", "Playing": ""})

def currently_playing():
    """Original currently playing from community config"""
    status = " "
    data = {}
    try:
        data = json.loads(subprocess.getoutput("dbus-player-status"))
    except ValueError:
        pass
    
    if data:
        if "state" in data:
            status = f"{status} {STATE[data['state']]}"
        if "title" in data:
            status = f"{status} {data['title']}"
        if "artist" in data:
            status = f"{status} - {data['artist']}"
    else:
        status = ""
    
    return status


def _redraw_tab_bar(timer_id):
    """Redraw tab bar periodically"""
    for tm in get_boss().all_tab_managers:
        tm.mark_tab_bar_dirty()