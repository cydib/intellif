#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-26 11:14:20
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
# 运行前先请先安装python3第三方库:pip install mysqlclient

import os,MySQLdb, urllib.request

def getPicture(ip, port,username,password, database, tablename, souceid):
	db = MySQLdb.connect(host=ip, port=port,user=username, passwd=password, db=database,charset="utf8")
	sql = "select image_data from " + tablename + str(pro) + "and source_id= " + souceid + " order by time desc;"
	cursor = db.cursor()
	cursor.execute(sql)
	data = cursor.fetchall()
	os.system("[ -d Pic ] && rm -r Pic;mkdir Pic || mkdir Pic")
	num = 0
	for i in data:
		num += 1
		for j in i:
			if ("http://") not in j:
				j = "http://" + ip + j
				name = j.split("/")[9].split(".")[0]
				print("正在下载第 %d 张 %s" % (num, name + ".jpg"))
				urllib.request.urlretrieve(j, ".\\Pic\\%s.jpg" % str(name))
			else:
				name = j.split("/")[7]
				print("正在下载第 %d 张 %s" % (num, name))
				urllib.request.urlretrieve(j, ".\\Pic\\%s" % str(name))

if __name__ == '__main__':

	# 这一段是需要根据现场情况更改
	ip = '192.168.11.128'
	port = 3306
	username = 'root'
	password = 'introcks1234'
	database = "intellif_face"
	tablelist = ['t_face_24', 't_face_25', 't_face_26']  # 可以增加表名
	cameralist = ['3', '4', '5', '10']  # 可以增加souceid
	# 这一段是需要根据现场情况更改

	table_property = [" where ((gender & 112) / 16) <= 5 ", " where ((race & 112) / 16) <= 5 ",
					  " where ((accessories & 112) / 16) <= 5 ",
					  " where ((age & 112) / 16) <= 5 ", " where ((accessories & 28672) / 4096) <= 5 "]
	for tablename in tablelist:
		for pro in table_property:
			for souceid in cameralist:
				getPicture(ip, port,username, password, database, tablename, souceid)
