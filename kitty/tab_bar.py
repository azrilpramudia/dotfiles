import datetime
import subprocess
from kitty.fast_data_types import Screen
from kitty.tab_bar import (
    DrawData,
    ExtraData,
    TabBarData,
    draw_tab_with_powerline,
    draw_attributed_string,
    Formatter,
    as_rgb,
)
from kitty.boss import get_boss


# ================= TAB DRAW =================
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

    draw_tab_with_powerline(
        draw_data, screen, tab, before, max_title_length, index, is_last, extra_data
    )

    if is_last:
        draw_right_status(draw_data, screen)

    return screen.cursor.x

# ================= RIGHT STATUS =================
def draw_right_status(draw_data: DrawData, screen: Screen) -> None:
    draw_attributed_string(Formatter.reset, screen)

    cells = create_cells()
    if not cells:
        return

    # ---- ABSOLUTE RIGHT POSITION (REAL FIX) ----
    right_edge = screen.columns

    # perkiraan lebar status bar (cukup besar supaya tidak ketabrak)
    status_width = 39

    start_pos = right_edge - status_width
    if start_pos < screen.cursor.x:
        start_pos = screen.cursor.x

    screen.cursor.x = start_pos

    tab_bg = as_rgb(int(draw_data.inactive_bg))
    tab_fg = as_rgb(int(draw_data.inactive_fg))

    # left rounded separator
    screen.cursor.fg = tab_bg
    screen.draw("")

    # draw cells
    screen.cursor.bg = tab_bg

    for i, cell in enumerate(cells):

        if isinstance(cell, tuple):
            # colored cell (battery)
            color, text = cell
            screen.cursor.fg = as_rgb(color)
            screen.draw(f" {text} ")
        else:
            # normal cell
            screen.cursor.fg = tab_fg
            screen.draw(f" {cell} ")

        if i != len(cells) - 1:
            screen.cursor.fg = tab_fg
            screen.draw("|")

# ================= CELLS =================
def create_cells():
    cells = []

    battery = get_battery()
    if battery:
        cells.append(battery)

    git = get_git_branch()
    if git:
        cells.append(git)

    now = datetime.datetime.now()
    cells.append(now.strftime("%a %d %b"))
    cells.append(now.strftime("%H:%M"))

    return cells


# ================= BATTERY =================
def get_battery():
    try:
        capacity = subprocess.getoutput("cat /sys/class/power_supply/BAT0/capacity")
        status = subprocess.getoutput("cat /sys/class/power_supply/BAT0/status")
        pct = int(capacity)

        icon = "🔋"
        if status == "Charging":
            icon = "⚡"

        # One Dark Pro color palette
        if pct >= 80:
            color = 0x98c379  # green
        elif pct >= 50:
            color = 0xe5c07b  # yellow
        elif pct >= 25:
            color = 0xd19a66  # orange
        else:
            color = 0xe06c75  # red

        return (color, f"{icon} {pct}%")

    except Exception:
        return None


# ================= GIT BRANCH =================
def get_git_branch():
    try:
        boss = get_boss()
        window = boss.active_window
        if not window:
            return None

        # get real shell pid
        pid = window.child.pid

        # read working directory from /proc
        cwd = subprocess.getoutput(f"readlink -f /proc/{pid}/cwd")

        if not cwd:
            return None

        branch = subprocess.getoutput(
            f"git -C '{cwd}' rev-parse --abbrev-ref HEAD 2>/dev/null"
        )

        if branch and branch != "HEAD":
            return f" {branch}"

    except Exception:
        pass

    return None

