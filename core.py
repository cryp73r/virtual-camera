'''
    Camera Lagger by CRYP73R & ShiavngAG

'''

import cv2
import numpy as np
import time
import random
import pyvirtualcam

vid = cv2.VideoCapture(0)

with pyvirtualcam.Camera(width=640, height=480, fps=30) as cam:

    while True:
        rand = random.choice([0, 1, 2])
        ret, frame = vid.read()
        arr = np.array(frame)
        rgba=cv2.cvtColor(arr, cv2.COLOR_RGB2BGRA)
        time.sleep(rand)
        cam.send(rgba)
        cam.sleep_until_next_frame()

vid.release()
cv2.destroyAllWindows()