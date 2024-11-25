#!/usr/bin/env python
import time
import freenect
#import cv2
import frame_convert2

#cv2.namedWindow('Depth')
#cv2.namedWindow('Video')
print('Press ESC in window to stop')


def get_depth():
    return freenect.sync_get_depth()[0]


def get_video():
    return freenect.sync_get_video()[0]


while 1:
    print(get_depth().shape)
    print(get_video().shape)
    time.sleep(1/30)
    
