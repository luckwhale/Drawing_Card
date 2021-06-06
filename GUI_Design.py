# -*- coding = utf-8 -*-
# @Time : 2021/5/23 18:30
# Author : ZYK
# @File : GUI_Design.py
# @Software: PyCharm
# 引用部分
import tkinter as tk
from chouka import *
from config import *
from recognize import recognize


# 声明全局变量
global number  # 用于记录算命结果


# 创立初始界面
class BaseDesk:
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('Genshin Impact Get Cards')
        self.root.geometry('400x300')

        InitFace(self.root)


# 初始界面的设置
class InitFace:
    def __init__(self, master):
        self.master = master
        self.master.config()
        # 初始界面initface
        self.initface01 = tk.Frame(self.master, )
        self.initface02 = tk.Frame(self.master, )
        self.initface01.pack()
        self.initface02.pack()
        init_label01 = tk.Label(self.initface01, text='你好！欢迎前来算命,你想抽谁', bg='yellow', font=('Arial', 12), width=80,
                                height=3)
        init_label01.pack(side='top', fill='x')
        btn01 = tk.Checkbutton(self.initface01, text='可莉', padx='2', bg='red', font=('Arial', 12), width=40, height=2,
                               command=self.change)
        btn01.pack(side='left', anchor='nw', expand="no")
        btn02 = tk.Checkbutton(self.initface01, text='甘雨', padx='2', bg='blue', font=('Arial', 12), width=40, height=2,
                               command=self.change)
        btn02.pack(side='left', anchor='n', expand="no")
        btn03 = tk.Checkbutton(self.initface01, text='胡桃', padx='2', bg='red', font=('Arial', 12), width=40, height=2,
                               command=self.change)
        btn03.pack(side='left', anchor='nw', expand="no")
        btn04 = tk.Checkbutton(self.initface01, text='优菈', padx='2', bg='blue', font=('Arial', 12), width=40, height=2,
                               command=self.change)
        btn04.pack(side='left', anchor='nw', expand="no")
        self.klee = tk.PhotoImage(file='./data/genshin/klee.gif')
        self.ganyu = tk.PhotoImage(file='./data/genshin/ganyu.gif')
        self.hutao = tk.PhotoImage(file='./data/genshin/hutao.gif')
        self.youla = tk.PhotoImage(file='./data/genshin/youla.gif')
        frame02 = tk.Frame(self.initface02, height=100)
        frame02.pack(side='top')
        lable1 = tk.Label(self.initface02, image=self.klee)
        lable1.pack(side="left")
        lable2 = tk.Label(self.initface02, image=self.ganyu)
        lable2.pack(side="left")
        lable3 = tk.Label(self.initface02, image=self.hutao)
        lable3.pack(side="left")
        lable4 = tk.Label(self.initface02, image=self.youla)
        lable4.pack(side="left")

    # 用于切换至下一个界面
    def change(self):
        self.initface01.destroy()
        self.initface02.destroy()
        Face1(self.master)


# 中间界面，用于显示算命结果
class Face1:
    def __init__(self, master):
        self.master = master
        self.number = number
        self.master.config()
        self.face1 = tk.Frame(self.master, )
        self.face1.pack(side='top')
        btn_chouka = tk.Button(self.face1, text='抽卡开始，祝你好运', command=self.begin)
        btn_chouka.pack(side="top")
        if self.number == 1:
            self.ouhuang = tk.PhotoImage(file='./data/outlook/ouhuang.gif')
            lable21 = tk.Label(self.face1, image=self.ouhuang)
            lable21.pack()
        else:
            self.feiqiu = tk.PhotoImage(file='./data/outlook/feiqiu.gif')
            lable22 = tk.Label(self.face1, image=self.feiqiu)
            lable22.pack()

    # 用于切换至抽卡页面
    def begin(self):
        self.face1.destroy()
        Face2(self.master)


# 抽卡页面
class Face2:
    def __init__(self, master):
        self.master = master
        self.number = number
        self.master.config()
        # 用于显示界面
        self.face2 = tk.Frame(self.master, )
        self.face2.pack(side='top')
        # 用于显示按钮
        self.face3 = tk.Frame(self.master, )
        self.face3.pack(side='top')

        self.character = tk.PhotoImage(file='./data/chouka/youla_chouka.gif')
        self.lable21 = tk.Label(self.face2, image=self.character)
        # 为了保持对图片的引用而不被回收
        self.lable21.image = self.character
        self.lable21.pack(side='top')

        # 按钮设置
        # 加入lambda可以使用有参数的command
        self.lb2_text = "原石：" + '%d' % stone
        self.lb2 = Label(self.face2, text=self.lb2_text, font=('宋体', 24, 'bold'))
        self.lb2.place(relx=0.6, rely=0)
        self.ten_button = Button(self.face3, text='十连', font=('宋体', 24, 'bold'), command=lambda: ten(self.lb2))
        self.ten_button.grid(row=1, column=5, padx=20, pady=10)
        self.single_button = Button(self.face3, text='单抽', font=('宋体', 24, 'bold'), command=lambda: single(self.lb2))
        self.single_button.grid(row=1, column=4, padx=20, pady=10)

        # 菜单部分
        self.mainmenu = Menu(self.master)
        self.menuFile = Menu(self.mainmenu)  # 菜单分组 menuFile
        self.mainmenu.add_cascade(label="充值", menu=self.menuFile, font=('宋体', 16, 'bold'))
        self.menuFile.add_command(label="648", command=big_money, font=('宋体', 16, 'bold'))
        self.menuFile.add_command(label="324", command=small_money, font=('宋体', 16, 'bold'))
        self.menuFile.add_command(label="剩余金额", command=remain_money, font=('宋体', 16, 'bold'))
        self.menuFile.add_separator()  # 分割线
        self.menuFile.add_command(label="退出", command=self.master.destroy, font=('宋体', 16, 'bold'))

        self.menuEdit = Menu(self.mainmenu)  # 菜单分组 menuEdit
        self.mainmenu.add_cascade(label="历史记录", menu=self.menuEdit, font=('宋体', 16, 'bold'))
        self.menuEdit.add_command(label="5星", command=five_star, font=('宋体', 16, 'bold'))
        self.menuEdit.add_command(label="4星", command=four_star, font=('宋体', 16, 'bold'))
        self.menuEdit.add_command(label="抽卡记录", command=lambda: history_record(self.master), font=('宋体', 16, 'bold'))
        self.menuEdit.add_command(label="保底查询", command=lambda: minimum_guarantee(self.master), font=('宋体', 16, 'bold'))

        self.master.config(menu=self.mainmenu)
        # self.master.bind('Button-3', popupmenu)  # 根窗体绑定鼠标右击响应事件
        # self.master.mainloop()


# 主进程
if __name__ == '__main__':
    global number
    number = recognize()
    root = tk.Tk()
    BaseDesk(root)
    root.mainloop()
