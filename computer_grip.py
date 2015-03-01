import sys
import os

def thumbs_up():
    os.system("snake-solver")

def placeholder():
    print "Hello!"

gestures = {
            0 : placeholder,
            1 : placeholder,
            2 : placeholder,
            8 : placeholder,
            9 : thumbs_up
            }

def handle_pose(pose):

    gestures[pose]()




if __name__ == '__main__':
    main()
