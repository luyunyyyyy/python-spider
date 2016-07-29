#!/usr/bin/env python 
# -*- coding: utf-8 -*-  
import urllib2 
import cookielib
import urllib
import re
import sys
import picture_auto
import time
'''模拟登录'''
def getHtml(username,password):
	reload(sys)
	sys.setdefaultencoding("utf-8")
	# 防止中文报错

	CaptchaUrl = "http://202.118.31.197/ACTIONVALIDATERANDOMPICTURE.APPPROCESS?id=73.2550761274789"
	PostUrl = "http://202.118.31.197/ACTIONLOGON.APPPROCESS?mode="
	GetUrl = "http://202.118.31.197/ACTIONFINDSTUDENTINFO.APPPROCESS?mode=1&showMsg="
	# 验证码地址和post地址


	cookie = cookielib.CookieJar()
	handler = urllib2.HTTPCookieProcessor(cookie)
	opener = urllib2.build_opener(handler)
	# 将cookies绑定到一个opener  cookie由cookielib自动管理


	#username = '20154839'
	#password = '19961021'
	# 用户名和密码

	picture = opener.open(CaptchaUrl).read()
	# 用openr访问验证码地址,获取cookie

	pic_name = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
	local = open(pic_name, 'wb')
	local.write(picture)
	local.close()
	# 保存验证码到本地
	SecretCode = picture_auto.image_to_string(pic_name)
	#SecretCode = raw_input('输入验证码： ')
	# 打开保存的验证码图片 输入
	print SecretCode + "此次验证码为"
	postData = {
		'WebUserNO':username,
		'applicant':'',
		'Password':password,
		'Agnomen':SecretCode,
		'submit7':'%B5%C7%C2%BC',
	}
	# 根据抓包信息 构造表单

	headers = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language': 'zh-CN,zh;q=0.8',
		'Connection': 'keep-alive',
		'Content-Type': 'application/x-www-form-urlencoded',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
	}
	# 根据抓包信息 构造headers


	data = urllib.urlencode(postData)
	# 生成post数据 ?key1=value1&key2=value2的形式
	request = urllib2.Request(PostUrl, data, headers)
	# 构造request请求

	try:
		response = opener.open(request)
		#result = response.read().decode('GBK')
		result = opener.open(GetUrl).read().decode('GBK')
		# 由于该网页是gb2312的编码，所以需要解码
		print result
		return result
		# 打印登录后的页面
	except urllib2.HTTPError, e:
		print e.code
		return null
	# 利用之前存有cookie的opener登录页面
	
