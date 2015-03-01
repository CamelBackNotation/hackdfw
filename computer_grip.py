import sys
import os

gestures = {
            0 : "Rest",
            1 : "Index?",
            2 : "Fuck you!",
            8 : "Thumbs down",
            9 : "Thumbs UP"
            }

def handle_pose(pose):

    print gestures[pose]




if __name__ == '__main__':
    main()
