# -*- coding = utf-8 -*-
# @Time : 2021/5/9 14:59
# Author : ZYK
# @File : get_data.py
# @Software: PyCharm
import cv2
import sys


def CatchPICFromVideo(window_name, catch_pic_num, path_name):
    cv2.namedWindow(window_name)

    # 视频来源，使用笔记本自带的摄像头
    cap = cv2.VideoCapture(0)

    # 告诉OpenCV使用人脸识别分类器，我使用pycharm里的的
    classfier = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    classfier.load('F:\\Miniconda\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml')
    # 识别出人脸后要画的边框的颜色，RGB格式
    color = (0, 255, 0)
    num = 0
    while cap.isOpened():
        ok, frame = cap.read()  # 读取一帧数据
        if not ok:
            break

            # 将当前帧转换成灰度图像,注意CV的格式式BGR的
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 人脸检测
        # scaleFactor是图像尺寸减小比例，minNeighbors是最少检测成功几次才算被识别，minsize是目标（人脸）的最小尺寸
        faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(faceRects) > 0:  # 大于0则检测到了人脸
            for faceRect in faceRects:  # 单独框出每一张人脸
                x, y, w, h = faceRect
                # 画一个矩形
                # cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
                # 将当前帧保存为图片
                img_name = '%s/%d.jpg' % (path_name, num)
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                cv2.imwrite(img_name, image)
                num += 1
                if num > catch_pic_num:  # 如果超过指定最大保存数量退出循环
                    break
                # 画出矩形框
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)

                # 显示当前捕捉到了多少人脸图片了
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, 'num:%d' % num, (x + 30, y + 30), font, 1, (255, 0, 255), 4)

        # 超过指定最大保存数量结束程序
        if num > catch_pic_num:
            break

        # 显示图像
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break

    # 释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage:%s camera_id face_num_max path_name\r\n" % (sys.argv[0]))
    else:
        CatchPICFromVideo("get_face", 600, 'C:\\Users\\lglin\\PycharmProjects\\pythonProject1\\data\\Other_Picture')
