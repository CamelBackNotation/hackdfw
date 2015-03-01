import sys
import subprocess
import os
import webbrowser
from pykeyboard import PyKeyboard

active = True
# Neutral-Toggle - 0
def toggle():
    global active
    active = not active
    print "Active is now: ", active


# Alt-Tab - 3
def swipe():
    k = PyKeyboard()
    k.press_key(k.alt_key)
    k.tap_key(k.tab_key)
    k.release_key(k.alt_key)

# Chrome - 2
def open_palm():
    # url = "http://google.com"
    url = "http://i.imgur.com/dlUr2Hl.gifv"
    webbrowser.open(url,new=2)

# Snake Solver - 0
def middle_finger():
    a = subprocess.check_output("pgrep -af python", shell=True)
    if not "start.py" in a:
        os.system("snake-solver")

# Spotify - 9
def thumbs_up():
    os.system("spotify &")


def placeholder():
    print "Hello!"

gestures = {
        0 : toggle,
        1 : middle_finger,
        2 : open_palm,
        3 : placeholder,
        8 : placeholder,
        9 : thumbs_up
    }

def handle_pose(pose):
    global active
    if pose == 0:
        toggle()
    elif active:
        gestures[pose]()




if __name__ == '__main__':
    main()
