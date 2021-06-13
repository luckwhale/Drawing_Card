# -*- coding = utf-8 -*-
# @Time : 2021/5/28 13:48
# Author : ZYK
# @File : music_player.py
# @Software: PyCharm
import pygame as py


def voice():
    py.mixer.init()
    # 文件加载
    py.mixer.music.load('./Video/4.mp3')
    # 播放，第一个是播放值 -1代表循环播放， 第二个参数代表开始播放的时间
    py.mixer.music.play(loops=0, start=0)
    while 1:  # 一定要有whlie让程序暂停在这，否则会自动停止
        pass
