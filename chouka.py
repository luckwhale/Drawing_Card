# -*- coding = utf-8 -*-
# @Time : 2021/5/25 15:54
# Author : ZYK
# @File : chouka.py
# @Software: PyCharm
import random
from tkinter import *
from Video import shipin
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

    stone = stone - 60
    i = random.random()
    times = times + 1
    this_time4 = this_time4 + 1
    if i < 0.006 * (number + 0.5) or times == 90:  # 五星中奖概率为0.6%
        a = random.random()
        p1 = multiprocessing.Process(target=shipin)
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
        cha = random.randint(0, len(cha_4) - 1)
        star = cha_4[cha]
        have4.append(star)
        this_time4 = 0
    elif i < 0.056 * (number + 0.5) or this_time4 == 10:  # 四星武器概率为2.55%
        wea = random.randint(0, len(weapon_4) - 1)
        star = weapon_4[wea]
        have4.append(star)
        this_time4 = 0
    else:  # 三星
        wea = random.randint(0, len(weapon_3) - 1)
        star = weapon_3[wea]
    # 不要使用p2的进程join()

    add(star, lb2)


def ten(lb2):
    """十连函数"""
    global stone
    if stone >= 1600:
        del get[:]
        for num in range(0, 10):  # 操作十次
            single(lb2)
        stone -= 1600
        print(get)
    else:
        print('您的原石不足，请充值！')


def add(star, lb2):
    """每次抽卡完毕的常规操作"""
    get.append(star)  # 将抽到的物品加入单次显示
    have.append(star)  # 将抽到的内容加入背包
    lb2_text = "原石：" + '%d' % stone
    lb2.config(text=lb2_text)
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

"""
if __name__ == '__main__':
    root = Tk()
    root.title('菜单实验')
    root.geometry('320x240')

    lb2_text = "原石：" + '%d' % stone
    lb2 = Label(root, text=lb2_text, font=('宋体', 32, 'bold'))
    lb2.place(relx=0.8, rely=0.1)
    single_button = Button(root, text='单抽', font=('宋体', 24, 'bold'), command=single)
    single_button.place(relx=0.7, rely=0.8)
    ten_button = Button(root, text='十连', font=('宋体', 24, 'bold'), command=ten)
    ten_button.place(relx=0.8, rely=0.8)

    # 菜单部分
    mainmenu = Menu(root)
    menuFile = Menu(mainmenu)  # 菜单分组 menuFile
    mainmenu.add_cascade(label="充值", menu=menuFile, font=('宋体', 16, 'bold'))
    menuFile.add_command(label="648", command=big_money, font=('宋体', 16, 'bold'))
    menuFile.add_command(label="324", command=small_money, font=('宋体', 16, 'bold'))
    menuFile.add_command(label="剩余金额", command=remain_money, font=('宋体', 16, 'bold'))
    menuFile.add_separator()  # 分割线
    menuFile.add_command(label="退出", command=root.destroy, font=('宋体', 16, 'bold'))

    menuEdit = Menu(mainmenu)  # 菜单分组 menuEdit
    mainmenu.add_cascade(label="历史记录", menu=menuEdit, font=('宋体', 16, 'bold'))
    menuEdit.add_command(label="5星", command=five_star, font=('宋体', 16, 'bold'))
    menuEdit.add_command(label="4星", command=four_star, font=('宋体', 16, 'bold'))
    menuEdit.add_command(label="抽卡记录", command=history_record(), font=('宋体', 16, 'bold'))
    menuEdit.add_command(label="保底查询", command=minimum_guarantee(root), font=('宋体', 16, 'bold'))

    root.config(menu=mainmenu)
    root.bind('Button-3', popupmenu)  # 根窗体绑定鼠标右击响应事件
    root.mainloop()
"""
