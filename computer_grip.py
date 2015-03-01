import sys
import subprocess
import os

def spotify():
    os.system("spotify")

def thumbs_up():
    a = subprocess.check_output("pgrep -af python", shell=True)
    if not "start.py" in a:
        os.system("spotify &")


def placeholder():
    print "Hello!"

gestures = {
            0 : placeholder,
            1 : placeholder,
            2 : spotify,
            8 : placeholder,
            9 : thumbs_up
            }

def handle_pose(pose):

    gestures[pose]()




if __name__ == '__main__':
    main()
