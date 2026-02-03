#!/usr/bin/env python3
"""Test Global Options Menu"""
import curses
import sys
sys.path.insert(0, '/home/user/.work/Code/arsenal')

from arsenal.modules.gui import GlobalOptionsMenu, Gui

def test_menu(stdscr):
    """Test the global options menu"""
    # Initialize
    Gui.init_colors()
    stdscr.clear()
    
    # Create menu
    menu = GlobalOptionsMenu(None)
    
    # Show initial state
    stdscr.addstr(0, 0, "Testing Global Options Menu...")
    stdscr.addstr(1, 0, f"Found {len(menu.common_vars)} variables")
    stdscr.addstr(2, 0, "Press any key to open menu...")
    stdscr.refresh()
    stdscr.getch()
    
    # Run menu
    menu.run(stdscr)
    
    # Show results
    stdscr.clear()
    stdscr.addstr(0, 0, "Menu closed. Values:")
    for idx, var in enumerate(menu.common_vars):
        value = menu.values.get(var, "")
        if value:
            stdscr.addstr(idx + 1, 0, f"{var}: {value}")
    stdscr.addstr(len(menu.common_vars) + 2, 0, "Press any key to exit...")
    stdscr.refresh()
    stdscr.getch()

if __name__ == '__main__':
    curses.wrapper(test_menu)
