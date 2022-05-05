# Replaced with updated code and customized monitor specs

import cv2
import time
import os
from PIL import ImageGrab

start_time = time.time()
display_time = 0.5

def ensure_dir():
    directory = os.path.dirname('./datasets/osrs/')
    print(directory)
    if not os.path.exists('./datasets/osrs/'):
        os.makedirs('./datasets/osrs/')

ensure_dir()

img = 0
mob = 'cow'
while img < 10:

    # -- include('examples/showgrabfullscreen.py') --#

    if __name__ == '__main__':
        # grab fullscreen
        im = ImageGrab.grab([0, -1075, 1920, 0], all_screens=True)
        # save image file
        im.save(r'./datasets/osrs/' + mob + '_' + str(img) + '.jpg', 'jpeg')

        # show image in a window
        # im.show()
    # -#
    img += 1

    time.sleep(display_time)
    if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break