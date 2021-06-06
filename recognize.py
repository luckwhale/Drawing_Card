# -*- coding = utf-8 -*-
# @Time : 2021/5/19 20:56
# Author : ZYK
# @File : recognize.py
# @Software: PyCharm
import cv2
import sys
from train import Model


def recognize():
    import cv2
    from train import Model
    global faceID
    # 加载模型
    model = Model()
    model.load_model(file_path='./zyk.face.model.h5')

    # 捕获指定摄像头的实时视频流
    cap = cv2.VideoCapture(0)

    # 人脸识别分类器本地存储路径
    cascade_path = "F:\\Miniconda\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml"
    flag = 0
    answer = 0
    # 检测识别人脸
    while True:
        ret, frame = cap.read()  # 读取一帧视频

        if ret is True:

            # 图像灰化，降低计算复杂度
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            continue
        # 使用人脸识别分类器，读入分类器
        cascade = cv2.CascadeClassifier(cascade_path)



        # 利用分类器识别出哪个区域为人脸
        faceRects = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(faceRects) > 0:
            for faceRect in faceRects:
                x, y, w, h = faceRect

                # 截取脸部图像提交给模型识别这是谁
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                faceID = model.face_predict(image)
                flag = flag + 1
                if faceID ==1:
                    answer = 1
                # 释放摄像头并销毁所有窗口
        if flag > 10:
            cap.release()
            return answer
