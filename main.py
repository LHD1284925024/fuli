#coding=utf-8
import requests
import re
import img
import logging
import variables
import db
import soup

logging.basicConfig(level=logging.ERROR, filename='error.log')
requests.packages.urllib3.disable_warnings()

def page_locate_get():
	a = db.select("img_pages")
	for url in a:
		print "\n=>正在解析id=="+str(url[0])+"页面"
		url = soup.page_realize(url[1])
		print "解析成功"
		for li in url:
			print "\n该本子链接为"+str(li[0])
			print "=>正在写进数据库中....."
			db.insert_img_locate('img_locate',variables.URL+li[0],0,li[1])

def img_get():
	url = db.condition_select('img_locate','where live = 0')
	for li in url:
		img.img(li[1],li[0],li[3])


page_locate_get()
img_get()