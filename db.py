#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import os
import sys
import psycopg2
import time

database='fuli'
user = 'smalt'
password=''
host='localhost'
port='5432'
conn = 0

def connectPostgreSQL():
    conn = psycopg2.connect(database=database,user=user,
        password=password,host=host,port=port
        )
    print '=>连接成功'
    print '=>数据库:'+database
    print '=>用户:'+user
    return conn

def createTable(string):
    conn = connectPostgreSQL()
    print '=>创建数据库........'
    cursor = conn.cursor()
    cursor.execute(string)
    conn.commit()
    conn.close()
    print '=>创建成功'

def dropTable(table):
    conn = connectPostgreSQL()
    print '=>删除数据库........'
    cursor = conn.cursor()
    cursor.execute("drop table "+table)
    conn.commit()
    conn.close()
    print '=>删除成功'

def insert(table,link,live):
    conn = connectPostgreSQL()
    print '=>插入新数据........'
    cursor = conn.cursor()
    cursor.execute("Insert into public."+table+"(link,live) values('"+link+"',"+str(live)+")")
    conn.commit()
    conn.close()
    print '=>插入成功'

def insert_img_locate(table,link,live,name):
    conn = connectPostgreSQL()
    print '=>插入新数据........'
    cursor = conn.cursor()
    cursor.execute("Insert into public."+table+"(link,live,name) values('"+link+"',"+str(live)+",'"+name+"')")
    conn.commit()
    conn.close()
    print '=>插入成功'

def select(table):
    conn = connectPostgreSQL()
    print '=>查询数据中........'
    cursor = conn.cursor()
    cursor.execute("select * from "+table)
    rows = cursor.fetchall()
    conn.close()
    print '=>查询成功'
    return rows

def condition_select(table,string):
    conn = connectPostgreSQL()
    print '=>查询数据中........'
    cursor = conn.cursor()
    cursor.execute("select * from "+table+" "+string)
    rows = cursor.fetchall()
    conn.close()
    print '=>查询成功'
    return rows

def update(table,name,value,id):
    conn = connectPostgreSQL()
    print '=>更新数据中........'
    cursor = conn.cursor()
    cursor.execute("update public."+table+" set "+name+" = '"+str(value)+"' where id ="+str(id))
    conn.commit()
    conn.close()
    print '=>修改成功'

def delete(table,id):
    conn = connectPostgreSQL()
    print '=>删除数据中........'
    cursor = conn.cursor()
    cursor.execute("delete from public."+table+" where id ="+str(id))
    conn.commit()
    conn.close()
    print '=>删除成功'

if __name__=='__main__':
    createTable("create table public.img_pages(id serial primary key,link varchar(255) not null,live integer not null)")
    createTable("create table public.img_locate(id serial primary key,link varchar(255) not null,live integer not null,name text not null)")
    for i in range(1,183+1):
        insert('img_pages','http://www.pppp83.com/p04/list_'+str(i)+'.html',0)