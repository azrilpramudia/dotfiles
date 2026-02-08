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
    """Draw right status mentok ke kanan"""
    draw_attributed_string(Formatter.reset, screen)
    
    cells = create_cells()
    if not cells:
        return
    
    # Build status text
    status_text = " | ".join(str(c[1]) if isinstance(c, tuple) else str(c) for c in cells)
    full_status = f" {status_text} "
    
    # Hitung lebar status tanpa icon
    base_width = len(full_status)
    
    # Hitung jumlah icon dari cells
    icon_count = 0
    for cell in cells:
        cell_text = str(cell[1]) if isinstance(cell, tuple) else str(cell)
        # Cek apakah cell ini adalah git branch (dimulai dengan space + icon)
        if cell_text.strip().startswith('') or '' in cell_text:
            icon_count += 1
    
    # Total width
    status_width = base_width + icon_count
    separator_width = -3  # ""
    
    total_width = separator_width + status_width    
    right_pos = screen.columns - total_width
    
    if right_pos < screen.cursor.x:
        right_pos = screen.cursor.x
    
    # Set posisi cursor
    screen.cursor.x = right_pos
    
    # Colors
    tab_bg = as_rgb(int(draw_data.inactive_bg))
    tab_fg = as_rgb(int(draw_data.inactive_fg))
    default_bg = as_rgb(int(draw_data.default_bg))
    
    # Draw separator
    screen.cursor.fg = tab_bg
    screen.cursor.bg = default_bg
    screen.draw("")
    
    # Draw status
    screen.cursor.fg = tab_fg
    screen.cursor.bg = tab_bg
    screen.draw(full_status)

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