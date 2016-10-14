#coding=utf-8
import requests
import re
import os
import shutil
import html_get
import variables
import logging
import db

ID = 0
NAME = ''

def getImg(html):
            reg = r'src="(.+?\.jpg)"'
            imgre = re.compile(reg)
            imglist = imgre.findall(html.text) 
            for i,v in enumerate(imglist):
                    print "\n=>"
                    print "开始下载该url下第"+str(i+1)+"张图片........"
                    downloader(v,i)
            print "\n更新数据live状态中...."
            db.update('img_locate','live',1,ID)

def downloader(url,i):
    try:
        r = requests.get(url, stream=True,timeout=30)
        if r.status_code == 200:
            print("status 验证成功")
            path = os.path.join(variables.IMG_STORE,str(NAME))
            variables.check_dir(path)
            with open(os.path.join(path,str(i).zfill(2) + '.jpg'), 'wb') as f:
                	shutil.copyfileobj(r.raw, f)
            print "第"+str(i+1)+"张图片下载完成!"
    except Exception:
        print("status code not 200")
        logging.exception("发生错误在该"+url+"下的第"+str(i+1)+"图片")

def img(url,id,name):
    global ID
    global NAME
    ID = id
    NAME = name
    print "\n\n=>"
    print "=>"
    print '正在解析id=='+str(ID)+'的url记录'
    print '该地址为'+url
    html = html_get.getHtml(url)
    getImg(html)
