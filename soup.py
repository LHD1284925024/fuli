#coding=utf-8
import requests
import html_get
import variables
import re
from bs4 import BeautifulSoup

def getSoup(url):
	html = html_get.getHtmlText(url)
	return BeautifulSoup(html)

def getAimUrl(url):
	soup = getSoup(url).find(text=variables.AIM).find_parents("a")
	return getFirstHref(soup[0])

def getFirstHref(soup):
	return soup['href']

def getAllHref(soup):
	return soup.find_all('a')

def page_realize(url):
	soup = getSoup(url)
	list = soup.find_all("div",class_="typelist")[0].find_all('a')
	hrefs = []
	a = []
	for i,v in enumerate(list):
		a.append(v.attrs['href'])
		a.append(v.text)
		hrefs.append(a)
		a = []
	return hrefs


