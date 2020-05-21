import json
import curses

#Set up stuff
banner = """
   ______           __     ____
  / __/ /____ ___ _/ /__  / __/__ ___ _________
 _\ \/ __/ -_) _ `/  '_/ _\ \/ _ `/ // / __/ -_)
/___/\__/\__/\_,_/_/\_\ /___/\_,_/\_,_/\__/\__/"""

#Set up curses window
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

#Create a window to store the banner in
bannerwin = curses.newwin(6, 49, 0, curses.COLS // 2 - 49 // 2)
bannerwin.addstr(0, 0, banner, curses.A_BOLD)
screen.refresh()
bannerwin.refresh()

curses.curs_set(0)

#Event loop
while True:
    k = screen.getch()
    if k == ord("q") or k == ord("Q"):
        curses.endwin()
        quit()
