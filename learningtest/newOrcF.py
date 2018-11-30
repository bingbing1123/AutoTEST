#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author:jiyanjiao

from aip import AipOcr
import cv2
from learningtest.new_commonfile import *
import learningtest.new_commonfile as gl


APP_ID = '14860096'
API_KEY = 'ZGTZiLghf4waPChqs69Ql3aR'
SECRET_KEY = 'azwmLsVrpGs5lMW8Ykd9DnR1tXc0TcPW'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

"""识别图片里的文字"""

def img_to_str(image_path):
    print("调用了img_to_str()方法")
    image = get_file_content(image_path)
    gl.gAllResult = client.general(image)
    #print("img_to_str(image_path):中的gAllResult===",gl.gAllResult)
    #return gAllResult

"""打开文件"""



def get_all_results():
    print("调用了get_all_results()的方法")
    count = 0
    str_result = ""
    #print("get_all_results()方法里的gAllResult",gl.gAllResult)
    print('words_resultin gAllResult======',('words_result'in gl.gAllResult))
    if 'words_result' in gl.gAllResult:
        #print("if 'words_result' in gAllResult:====",gl.gAllResult)
        for w in gl.gAllResult['words_result']:
            if str_result =="":
                str_result = w['words']
            else:
                str_result = str_result +'\n' + w['words']
            count = count +1
    str_result = str_result + '\n' + "总计：" + str(count)
    return str_result


def get_one_str(contains_str):
    print("是否走了get_one_str(contains_str)函数")
    key = []
    gl.gOneResult = []
    count = 0
    str_result = ""
    print("get_one_str(contains_str)函数里的gAllResult",gl.gAllResult)
    if 'words_result' in gl.gAllResult:
        for  w in gl.gAllResult['words_result']:
            print("w为-----------",w)
            if contains_str in w['words']:
                key.append(w['words'])
                gl.gOneResult.append(w['location'])
                count = count +1
    for i in range(0,len(key)):
        if str_result =="":
            str_result = key[i]
        else:
            str_result = str_result + '\n' +key[i]
    return str_result + '\n' +"总计："+str(count)

    """
    text_results = []
    print("调用了results")
    #image = get_file_content(fname)

  
    #words_results = client.general(image)

    print("words_results ===========",gAllResult)
    results = gAllResult["words_result"]
    print("results===========",results)

    img = cv2.imread(fname)
    for result in results:
        text = result["words"]
        print("text==",text)
        location = result["location"]
        text_results.append(text)


        # 画矩形框
        cv2.rectangle(img, (location["left"],location["top"]), (location["left"]+location["width"],location["top"]+location["height"]), (0,255,0), 2)

    cv2.imwrite(fname[:-4]+"_result.jpg", img)
    return text_results
    """





if __name__ == '__main__':
    pathf = gPicturePath
    s = img_to_str(pathf)
    #gAllResult = s
    #get_one_str("腻柔滑滋润呵护")
    get_all_results()