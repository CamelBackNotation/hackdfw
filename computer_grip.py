import sys
import subprocess
import os
import webbrowser

# Chrome - 2
def open_palm():
    url = "http://google.com"
    webbrowser.open(url,new=2)

# Snake Solver - 0
def middle_finger():
    a = subprocess.check_output("pgrep -af python", shell=True)
    if not "start.py" in a:
        os.system("snakesolver")

# Spotify - 9
def thumbs_up():
    os.system("spotify &")


def placeholder():
    print "Hello!"

gestures = {
        0 : middle_finger,
        1 : placeholder,
        2 : open_palm,
        8 : placeholder,
        9 : thumbs_up
    }

def handle_pose(pose):

    gestures[pose]()




if __name__ == '__main__':
    main()
