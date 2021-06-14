# -*- coding = utf-8 -*-
# @Time : 2021/5/25 15:54
# Author : ZYK
# @File : chouka.py
# @Software: PyCharm
import random
from tkinter import *
from video import shipin
import multiprocessing
from music_player import voice
from config import *


# 抽卡部分的函数

def single(lb2):
    """单抽系统"""
    global times
    global this_time4
    global this_time5
    global stone
    global number
    global status
    global star_status

    stone = stone - 60
    i = random.random()
    times = times + 1
    this_time4 = this_time4 + 1
    num = 0
    if i < 0.006 * (number + 0.5) or times == 90:  # 五星中奖概率为0.6%
        a = random.random()
        star_status = 5
        if status :
            num = 5
            p1 = multiprocessing.Process(target=shipin(num))
            p2 = multiprocessing.Process(target=voice)
            p1.start()
            p2.start()
            p1.join()
            p1.terminate()
            p2.terminate()
        if a < 0.5 or this_time5:
            star = st5[0]
            have5.append(star)
            this_time5 = 0  # 大保底用过了
            times = 0
        else:
            a = random.randint(1, 5)
            star = st5[a]
            have5.append(star)
            this_time5 = 1  # 大保底开始
            times = 0

    elif i < 0.031 * (number + 0.5) or this_time4 == 10:  # 四星角色概率为2.55%
        if status:
            num = 4
            p1 = multiprocessing.Process(target=shipin(num))
            p2 = multiprocessing.Process(target=voice)
            p1.start()
            p2.start()
            p1.join()
            p1.terminate()
            p2.terminate()
        cha = random.randint(0, len(cha_4) - 1)
        star = cha_4[cha]
        have4.append(star)
        this_time4 = 0
    elif i < 0.056 * (number + 0.5) or this_time4 == 10:  # 四星武器概率为2.55%
        if status:
            num = 4
            p1 = multiprocessing.Process(target=shipin(num))
            p2 = multiprocessing.Process(target=voice)
            p1.start()
            p2.start()
            p1.join()
            p1.terminate()
            p2.terminate()
        wea = random.randint(0, len(weapon_4) - 1)
        star = weapon_4[wea]
        have4.append(star)
        this_time4 = 0
    else:  # 三星
        if status:
            num = 3
            p1 = multiprocessing.Process(target=shipin(num))
            p2 = multiprocessing.Process(target=voice)
            p1.start()
            p2.start()
            p1.join()
            p1.terminate()
            p2.terminate()
        wea = random.randint(0, len(weapon_3) - 1)
        star = weapon_3[wea]

    add(star, lb2)


def ten(lb2):
    """十连函数"""
    global stone
    global status
    global star_status
    # 用于记录用户是十连还是单抽
    status = 0
    if stone >= 1600:
        del get[:]
        for num in range(0, 10):  # 操作十次
            single(lb2)
        stone -= 1600
        print(get)
        if star_status == 4:
            p1 = multiprocessing.Process(target=shipin(4))
            p2 = multiprocessing.Process(target=voice)
            p1.start()
            p2.start()
            p1.join()
            p1.terminate()
            p2.terminate()
        else :
            p1 = multiprocessing.Process(target=shipin(5))
            p2 = multiprocessing.Process(target=voice)
            p1.start()
            p2.start()
            p1.join()
            p1.terminate()
            p2.terminate()
    else:
        print('您的原石不足，请充值！')
    # 重置抽卡状态
    status = 1
    star_status = 4

def add(star, lb2):
    """每次抽卡完毕的常规操作"""
    get.append(star)  # 将抽到的物品加入单次显示
    have.append(star)  # 将抽到的内容加入背包
    lb2_text = "原石：" + '%d' % stone
    lb2.config(text=lb2_text)
    # 由于游戏是一次性的，选择不将结果存在文件中，想存的可以放开注释
    # with open('./data/Record/history', 'w') as f:
    # f.write(star + '\n')
    # f.close()


# 显示部分的函数

def big_money():
    s = '请充值648元'
    # lb1.config(text=s)


def small_money():
    s = '请充值324元'
    # lb1.config(text=s)


def remain_money():
    temp = '%d' % debt
    s = '剩余金额:' + temp
    # lb1.config(text=s)


def five_star(root):
    s = '5星查看'
    # lb1.config(text=s)


def four_star(root):
    s = '4星查看'
    # lb1.config(text=s)


def history_record(root):
    global page
    winNew = Toplevel(root)
    winNew.geometry('600x600')
    winNew.title('历史记录')
    record = {}
    length = len(have)
    i = 0
    for i in range(0, 10):
        if page + i + 1 > length:
            break
        record['lb' + str(i)] = Label(winNew, text=have[page + i], font=('宋体', 16, 'bold'))
        record['lb' + str(i)].grid(row=i + 1)
    left_button = Button(winNew, text='向前翻页', command=lambda: updata_record(root, winNew, 0))
    left_button.grid(row=i + 2, column=1)
    right_button = Button(winNew, text='向后翻页', command=lambda: updata_record(root, winNew, 1))
    right_button.grid(row=i + 2, column=2)


def updata_record(root, winNew, status):
    global page
    winNew.destroy()
    if status == 1:
        if page + 10 > len(have):
            pass
        else:
            page = page + 10
    if status == 0:
        if page == 0:
            pass
        else:
            page = page - 10
    history_record(root)


def minimum_guarantee(root):
    s = '大保底:' + '%d' % (180 - 90 * this_time5 - times)
    k = '小保底' + '%d' % (90 - times)
    sk = s + '\n' + k
    winNew = Toplevel(root)
    winNew.geometry('320x240')
    winNew.title('保底查询')
    lb2 = Label(winNew, text=sk)
    lb2.place(relx=0.2, rely=0.2)
    btClose = Button(winNew, text='关闭', command=winNew.destroy)
    btClose.place(relx=0.7, rely=0.5)


# 用于实现鼠标右键打开菜单
# def popupmenu(event):
#    mainmenu.post(event.x_root, event.y_root)
