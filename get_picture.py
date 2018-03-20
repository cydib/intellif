# -*- coding: utf-8 -*-
import MySQLdb, urllib.request,os


def connectdb():
	db = MySQLdb.connect("192.168.11.65", "root", "introcks1234", "intellif_face")
	cursor = db.cursor()
	cursor.execute(
		"select f.image_data from intellif_face.t_face_24 f where  ((f.gender & 112) / 16) <= 5 order by time desc;")
	data = cursor.fetchall()
	os.system("cd F:\temp\pic\;rm *")
	num = 0
	for i in data:
		num += 1
		for j in i:
			j = "http://192.168.11.65" + j
			name = j.split("/")[9].split(".")[0]
			print("正在下载第 %d 张 %s"%(num,name+".jpg"))
			urllib.request.urlretrieve(j, "F:\\temp\\pic\\%s.jpg" %str(name))



connectdb()
