# -*- coding = utf-8 -*-
# @Time : 2021/5/27 16:10
# Author : ZYK
# @File : video.py
# @Software: PyCharm
import cv2
import os
import multiprocessing
from music_player import voice


def shipin():
    # 这部分主要是测试多进程用的可以删掉
    cap = cv2.VideoCapture('./Video/5star.mp4')
    print('进程pid=%d' % (os.getpid()))


    while (cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        res = cv2.resize(frame, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC)
        cv2.imshow('frame', res)
        if cv2.waitKey(5) & 0xFF == 27:  # 用esc退出
            break

    cap.release()
    cv2.destroyAllWindows()


