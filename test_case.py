import requests

def login():
	payload = {"username":"admin","password":"introcks" }
	r = requests.Session().post("http://192.168.11.59:3000/login",data=payload)
	print(r)


login()