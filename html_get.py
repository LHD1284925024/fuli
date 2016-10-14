#coding=utf-8
import requests
import re

def getHtml(url):
	req = requests.get(url)

	pattern = re.compile('^utf-8.*',re.I)

	if pattern.match(req.apparent_encoding):
		req.encoding = 'utf-8'
	return req

def getHtmlText(url):
	return getHtml(url).text