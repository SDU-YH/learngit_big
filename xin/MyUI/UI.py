import tkinter as tk
from tkinter import *
import matplotlib.pylab as pl
import webbrowser
import os
import turtle
from PIL import Image, ImageTk
import sys
sys.path.append(r'./MyData')
sys.path.append(r'./Tree')
'''
import RandomForest
from RandomForest import * '''
import Data_manage
from Data_manage import *



class BuDemo:
    def __init__(self, root):
        root.title("沙盘游戏分析系统")
        root.geometry("1000x490+300+150")
        self.myphoto=PhotoImage(file=r"C:\Users\15502\Desktop\A_f.png")
        self.RF = tk.Button(root,
                            activebackground="red",
                            anchor='n',
                            relief='raised',
                            text="心理分析",
                            fg="blue",
                            #font=（"宋体"，260）,
                            image=self.myphoto,
                            compound="center",
                            #height=10,
                            #width=34,
                            command=self.predict_rf)
        self.RF.pack(side="left")
        self.myphoto2=PhotoImage(file=r'C:\Users\15502\Desktop\B_f.png')

        self.RF = tk.Button(root,
                            text="开始游戏",
                            fg="red",
                            image=self.myphoto2,
                            compound="center",
                            #height=10,
                            #width=34,
                            command=self.openweb)
        self.RF.pack(side="left")
        self.Edata={}

    def predict_rf(self):
        self.nextpage=tk.Tk()
        self.nextpage.title("请回答问题")
        self.nextpage.geometry("300x300+500+250")
        self.L1=Label(self.nextpage,text="问题1")
        self.L1.pack()
        self.E1=Entry(self.nextpage,bd=3,width=70)
        self.E1.pack()
        self.L2=Label(self.nextpage,text="问题2")
        self.L2.pack()
        self.E2=Entry(self.nextpage,bd=3,width=70)
        self.E2.pack()
        self.L3=Label(self.nextpage,text="问题3")
        self.L3.pack()
        self.E3=Entry(self.nextpage,bd=3,width=70)
        self.E3.pack()
        self.L4=Label(self.nextpage,text="问题4")
        self.L4.pack()
        self.E4=Entry(self.nextpage,bd=3,width=70)
        self.E4.pack()
        self.L5=Label(self.nextpage,text="问题5")
        self.L5.pack()
        self.E5=Entry(self.nextpage,bd=3,width=70)
        self.E5.pack()
        self.button3=Button(self.nextpage,text="提交回答",command=self.updata)
        self.button3.pack()
        self.nextpage.mainloop()
    
        
    def openweb(self):
        webbrowser.open("https://lingxinyun.cn/psy/index.html#/HomePage")

    def updata(self):
        self.Edata[1]=self.E1.get()
        self.Edata[2]=self.E2.get()
        self.Edata[3]=self.E3.get()
        self.Edata[4]=self.E4.get()
        self.Edata[5]=self.E5.get()
        self.nextpage.destroy()
        #调用随机森林
        #调用随机森林分析数据

        
