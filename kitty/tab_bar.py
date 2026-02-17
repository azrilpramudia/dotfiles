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
    # if timer_id is None:
    #     timer_id = add_timer(_redraw_tab_bar, 2.0, True)

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
        (as_rgb(0x98C379), as_rgb(0x282C34)), 
        (as_rgb(0xE5C07B), as_rgb(0x282C34)), 
    ]
    
    default_bg = as_rgb(int(draw_data.default_bg))

    for i, cell in enumerate(cells):
        if i < len(cell_colors):
            current_bg, current_fg = cell_colors[i]
        else:
            current_bg, current_fg = cell_colors[-1]

        if i == 0:
            screen.cursor.fg = current_bg
            screen.cursor.bg = default_bg
            screen.draw("")
        else:
            prev_bg = cell_colors[i-1][0] if i-1 < len(cell_colors) else cell_colors[-1][0]
            screen.cursor.fg = current_bg
            screen.cursor.bg = prev_bg
            screen.draw("")

        # screen.cursor.bold = True
        screen.cursor.fg = current_fg
        screen.cursor.bg = current_bg
        screen.draw(f" {cell} ")
        # screen.cursor.bold = False

    draw_attributed_string(Formatter.reset, screen)

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
    cells.append(now.strftime("%I:%M"))
    
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