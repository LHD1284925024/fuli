#coding=utf-8
import os

URL = 'http://www.pppp83.com'
AIM = '动漫图片'

def dir_maker(dir):
	dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), dir)
	return check_dir(dir)

def check_dir(dir):
	if not os.path.exists(dir):
    		os.makedirs(dir)
    	return dir

PATH = dir_maker('lib')
IMG_STORE = dir_maker('lib/img')

