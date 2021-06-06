# -*- coding = utf-8 -*-
# @Time : 2021/5/28 13:25
# Author : ZYK
# @File : GUI_Tools.py
# @Software: PyCharm
import tkinter as tk  # 导入Tkinter
import tkinter.dnd as dnd


class dndIcon:
    def __init__(self, idname=None):
        self.idname = idname
        self.canvas = None
        self.label = None
        self.id = None

    def attach(self, canvas, x=10, y=10):
        if canvas is self.canvas:
            self.canvas.coords(self.id, x, y)
            return
        if self.canvas:
            self.detach()
        if not canvas:
            return
        id = canvas.create_window(x, y, window=self.idname, anchor="nw")
        self.canvas = canvas
        self.id = id
        self.idname.bind("<ButtonPress>", self.press)

    def detach(self):
        canvas = self.canvas
        if not canvas:
            return
        id = self.id
        label = self.label
        self.canvas = self.label = self.id = None
        canvas.delete(id)
        self.idname.place_forget()

    def press(self, event):
        if dnd.dnd_start(self, event):
            # where the pointer is relative to the label widget:
            self.x_off = event.x
            self.y_off = event.y
            # where the widget is relative to the canvas:
            self.x_orig, self.y_orig = self.canvas.coords(self.id)

    def move(self, event):
        x, y = self.where(self.canvas, event)
        self.canvas.coords(self.id, x, y)

    def putback(self):
        self.canvas.coords(self.id, self.x_orig, self.y_orig)

    def where(self, canvas, event):
        # where the corner of the canvas is relative to the screen:
        x_org = canvas.winfo_rootx()
        y_org = canvas.winfo_rooty()
        # where the pointer is relative to the canvas widget:
        x = event.x_root - x_org
        y = event.y_root - y_org
        # compensate for initial pointer offset
        return x - self.x_off, y - self.y_off

    def dnd_end(self, target, event):
        pass


# 可拖拽控件的控件
class dndwidget(tk.Frame):
    def __init__(self, master, **kw):
        tk.Frame.__init__(self, master, **kw)
        self.top = master
        self.canvas = tk.Canvas(self.top, width=100, height=100, **kw)
        self.canvas.pack(fill="both", expand=1)
        self.canvas.dnd_accept = self.dnd_accept

    def dnd_accept(self, source, event):
        return self

    def dnd_enter(self, source, event):
        self.canvas.focus_set()  # Show highlight border
        x, y = source.where(self.canvas, event)
        x1, y1, x2, y2 = source.canvas.bbox(source.id)
        dx, dy = x2 - x1, y2 - y1
        self.dndid = self.canvas.create_rectangle(x, y, x + dx, y + dy)
        self.dnd_motion(source, event)

    def dnd_motion(self, source, event):
        x, y = source.where(self.canvas, event)
        x1, y1, x2, y2 = self.canvas.bbox(self.dndid)
        self.canvas.move(self.dndid, x - x1, y - y1)

    def dnd_leave(self, source, event):
        self.top.focus_set()  # Hide highlight border
        self.canvas.delete(self.dndid)
        self.dndid = None

    def dnd_commit(self, source, event):
        self.dnd_leave(source, event)
        x, y = source.where(self.canvas, event)
        source.attach(self.canvas, x, y)


def test2():
    root = tk.Tk()
    root.geometry('{}x{}+{}+{}'.format(800, 600, 250, 350))  # 改变窗口位置和大小
    root.title('dnd拖拽演示')
    v = htk.View(root, kind='田')
    v.pack()
    t1 = dndwidget(v.v[0])
    t2 = dndwidget(v.v[1], bg='green')
    t3 = dndwidget(v.v[2], bg='yellow')
    t4 = dndwidget(v.v[3], bg='blue')

    i1 = dnd.Icon("ICON1")
    i2 = dnd.Icon("ICON2")
    i3 = dnd.Icon("ICON3")
    bt = tk.Button(v.v[3], text="Quit")
    i4 = dndIcon(bt)

    i1.attach(t1.canvas)
    i2.attach(t2.canvas)
    i3.attach(t3.canvas)
    i4.attach(t4.canvas)
    root.mainloop()


if __name__ == '__main__':
    test2()
