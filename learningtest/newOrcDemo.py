#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author:jiyanjiao

import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageDraw, ImageFont
from learningtest.newOrcF import *
import learningtest.new_commonfile as gl
from tkinter import filedialog
import cv2
import numpy

path = os.path.abspath(".")
filename = path +"\\14.png" #修改了

root = tk.Tk()
frame = tk.Frame(root)
frame.place(x = 0, y = 0, width = 600, height = 600)

scroll = tk.Scrollbar(frame)
global ff

def open_files():
    img_rgb = filedialog.askopenfilename(title='打开文件', filetypes=[("All files", "*.*"),("All files", "*.*")])
    #ff = img_rgb
    if img_rgb !="":
        if '.png' in img_rgb or '.jpg' in img_rgb:
            #clear()
            img_gray = cv2.cvtColor(cv2.imread(img_rgb),cv2.COLOR_BGR2GRAY)
            #kernel = numpy.ones((5, 5), numpy.float32) / 25
            kernel = numpy.array([
                [-1, -1, -1, -1, -1],
                [-1, 2, 2, 2, -1],
                [-1, 2, 7, 2, -1],
                [-1, 2, 2, 2, -1],
                [-1, -1, -1, -1, -1]]) / 9.016
            dst = cv2.filter2D(img_gray,-1,kernel=kernel)
            cv2.imwrite(filename,dst)


            #cv2.imwrite(filename,img_gray,[int(cv2.IMWRITE_PNG_COMPRESSION), 5]) #修改了


            gl.gPicturePath = filename
            print('gl.gPicturePath===',gl.gPicturePath)
            gl.gFirstPicturePath = img_rgb
            print("gl.gFirstPicturePath==",gl.gFirstPicturePath)
            find_all()
        else:
            tkinter.messagebox.showinfo("提示","请选择格式为.jpg或者.png的图片")
    else:
        print("什么时候走的这有点奇怪")
        tkinter.messagebox.showinfo("提示","请正确选择图片")


def find_all():
    print("走到了find_all()")
    print("find_all()函数里的gFirstPicturePath====",gl.gFirstPicturePath)
    if gl.gFirstPicturePath:
        is_exist = os.path.exists(gl.gFirstPicturePath)
        print("is_exist===",is_exist)
        #text.delete(0,0,END)
        print("if gAllResult:====",gl.gAllResult)
        if gl.gAllResult:
            print("走到find_all()里的gAllResult==[]的分支了吗")
            print("img_to_str(gPicturePath)里的gPicturePath",gl.gPicturePath)
            result_str = get_all_results()
            choise_result_text.insert('end',result_str)
        elif is_exist:
            #print("fffffffffffff=========================",ff)
            img_to_str(gl.gPicturePath)
            result_str = get_all_results()
            choise_result_text.insert('end', result_str)
        #find_picture_all()
    else:
        tkinter.messagebox.showinfo("提示","请先读取图片")


def find_picture_all():
    if gl.gFirstPicturePath:
        print("gl====",gl.gAllResult)
        img_rgb = cv2.imread(gl.gPicturePath)
        merged = cv2.GaussianBlur(numpy.uint8(numpy.clip((1.0 * img_rgb - 60), 0, 200)), (0, 0), 3)
        pil_im = Image.fromarray(img_rgb)
        draw = ImageDraw.Draw(pil_im)
        font = ImageFont.truetype("FZYTK.TTF", 15, encoding="utf-8")
        for result in (gl.gAllResult)["words_result"]:
            location = result["location"]
            print("location=======",location)
            #merged = cv2.GaussianBlur(numpy.uint8(numpy.clip((1.0 * img_rgb - 60), 0, 200)), (0, 0), 3)
            cv2.rectangle(img_rgb, (location["left"], location["top"]),
                          (location["left"] + location["width"], location["top"] + location["height"]), (0, 255, 0), 2)
            cropImg = img_rgb[location["top"] - 5:location["top"] + location["height"] + 5,location["left"] - 5:location["left"] + location["width"] + 5]
            merged[location["top"] - 5:location["top"] + location["height"] + 5, location["left"] - 5:location["left"] + location["width"] + 5] = cropImg
        for result in (gl.gAllResult)["words_result"]:

            draw.text((location["left"], location["top"] + location["height"] + 20), "坐标位：%s,%s" %
                      (location["left"], location["top"]), (220, 40, 1), font=font)
            cv_text_im = cv2.cvtColor(numpy.array(pil_im), cv2.COLOR_RGB2BGR)
        cv2.imwrite(path+"ALL.png",cv_text_im)
    else:
        tkinter.messagebox.showinfo("提示:","请选择图片")
    root.title("ALL.png")  # 在这里修改窗口的标题
    cv2.imshow("Target", cv2.imread(path + "ALL.png"))


def find_one():
    if gl.gFirstPicturePath:
        contains_str = search_entry.get()
        print("contains_str = search_entry.get()获取的值为====",contains_str)
        if contains_str.strip() != "":
            is_exist = os.path.exists(gl.gPicturePath)
            #text.delete(0.0, END)
            if gl.gAllResult:
                result_str = get_one_str(contains_str)
                ocr_result_text.insert('end', result_str)
            elif is_exist:
                img_to_str(gl.gPicturePath)
                result_str = get_one_str(contains_str)
                ocr_result_text.insert('end', result_str)
            find_picture_one()
        else:
            tkinter.messagebox.showinfo('提示', '请输入想要搜索的关键词')
    else:
        tkinter.messagebox.showinfo('提示', '请先读取图片')

def find_picture_one():
    print("走到了find_picture_one()函数")
    left = []
    top = []
    height = []
    width = []
    print("for w in gl.gOneResult:===", gl.gOneResult)
    for w in gl.gOneResult:
        left.append(w['left'])
        top.append(w['top'])
        height.append(w['height'])
        width.append(w['width'])
    img_rgb = cv2.imread(gl.gPicturePath)
    merged = cv2.GaussianBlur(img_rgb, (17, 17), 0)
    #merged = cv2.GaussianBlur(numpy.uint8(numpy.clip((1.0 * img_rgb - 60), 0, 200)), (0, 0), 3)
    for i in range(0, len(left)):
        print("left[i]=============", left[i])
        cv2.rectangle(img_rgb, (left[i], top[i]), (left[i] + width[i], top[i] + height[i]),
                     (0, 30, 255), 5)
        merged[top[i]:top[i] + height[i], left[i]:left[i] + width[i]] = \
            img_rgb[top[i]:top[i] + height[i], left[i]:left[i] + width[i]]
    for j in range(0, len(left)):
        if j == 0:
            pil_im = Image.fromarray(merged)
        else:
            pil_im = Image.fromarray(cv_text_im)
        draw = ImageDraw.Draw(pil_im)
        font = ImageFont.truetype("FZYTK.TTF", 15, encoding="utf-8")
        draw.text((left[j]-5, top[j]-5 + height[j] +5), "坐标位：%s,%s" % (left[j], top[j]), (0,255,0), font=font)
        cv_text_im = cv2.cvtColor(numpy.array(pil_im), cv2.COLOR_RGB2BGR)
        print("cv2.imwrite(path + 2.png, cv_text_im)==",path + "2.png")
        cv2.imwrite(path + "2.png", cv_text_im)

    root.title("1.png")  # 在这里修改窗口的标题
    cv2.namedWindow("Target", 1)
    cv2.moveWindow("Target", 700, 100)
    cv2.imshow("Target", cv2.imread(path + "2.png"))
"""
def text_results(results):
    for i in range(len(results)):
        print("results[i]===",results[i])
        choise_result_text.insert(1.0,results[i]+'\n')
"""



root.title("图像识别工具")
root.geometry('600x700+10+10')      #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
root["bg"] = "#BC528C"                 #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
#root.attributes("-alpha",0.8)       #虚化 值越小虚化程度越高

choise_path_label = tk.Label(frame, text = "请选择指定图片:")
choise_path_label.grid(row = 0, column = 0)

choise_path_entry = tk.Entry(frame,width = 40)
choise_path_entry.grid(row = 0, column = 1,sticky=tk.W)

choise_path_button = tk.Button(frame, text = "选择图片",width=6,height=1,command=open_files)
choise_path_button.grid(row = 0,column = 2, sticky=tk.W)

choise_result_text = tk.Text(frame,width=45, height=20)
choise_result_text.grid(row=1, column=1,sticky=tk.W)



#img = Image.open('picture/en.jpg')
#photo = ImageTk.PhotoImage(img)
#imageview = tk.Label(frame, image= photo)
#imageview.grid(row = 1, column = 1,rowspan = 3, columnspan = 3,sticky=tk.W)

search_label = tk.Label(frame, text = "请输入搜索内容:")
search_label.grid(row = 4, column = 0)


search_entry = tk.Entry(frame,width = 40)
search_entry.grid(row = 4, column = 1,sticky=tk.W)

ocr_result_text = tk.Text(frame,width=45, height=20)
ocr_result_text.grid(row=5, column=1, rowspan=5, columnspan=5,sticky=tk.W)

scroll = tk.Scrollbar()

search_button = tk.Button(frame, text = "搜索单词",command=find_one,width=6,height=1)
search_button .grid(row = 4, column = 2,sticky=tk.W)

search_all_button = tk.Button(frame, text = "搜索全部",command=find_picture_all,width=6,height=1)
search_all_button .grid(row = 4, column = 3,sticky=tk.W)

root.mainloop()


