#chatnow.py 为主调用函数
from mylog import Mylog,logging
from webRequest import WebRequest
import os
# from pythFile import readFileName,file_name
righnote ='''
Copyright [2022] by [Michael]
1999-2025 All rights reserved.
'''




def runMain():
    url = "https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.0.0.5bb337f4jLMOOH&fsb=y&IndexArea=product_en&SearchText=solar+Inverter&tab=supplier"
    htmlObj = WebRequest(url)
    resp = htmlObj.getHTMLText()
    print(resp)

#*********************************路径处理************************************
print(righnote)
# print(os.getcwd())
path = os.getcwd()
#改变目录
os.chdir(path)
print(os.getcwd())
logging.info('开始:{}'.format(path))

runMain()





