#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import spider
print "hello "
print "输入模式 a，单独访问一个账号和密码 b，遍历全部账号"
str_mode = raw_input()
if str_mode == 'a':
    #name = str(raw_input("账号"))
    #password = str(raw_input("密码"))
    name = "20154839"
    password = "19961021"
    spider.getHtml(name,password)
else :
    temp_name = 20150001
    while temp_name <=20156000 :
        spider.getHtml(str(temp_name), str(temp_name))
