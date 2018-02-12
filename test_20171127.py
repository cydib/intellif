# -*- coding: utf-8 -*-
import requests,json,customer,test_sale
import random
from time import sleep


class TestYunJi:

	def __init__(self):
		self.base_url = "https://test.yj2025.com/ierp/"
		self.s = requests.Session()
		self.headers = {'content-type': 'application/json;charset=UTF-8'}


	def login(self,Llist):
		r = self.s.post(self.base_url + 'login',data=Llist)
		return self


	def switchAccount(self,Slist):
		r = self.s.get(self.base_url +'login/impersonate',params=Slist)
		return self


	# def add_customer(self):
	# 	r = self.s.post(self.base_url + "p/crm-pc/v1/pc/crm/customer/add",data=json.dumps(customer.cu_data),headers=self.headers)
	# 	print(r.status_code,r.text)


	# def getCustomerName(self):
	# 	r = self.s.post(self.base_url + "crm-pc/v1/pc/crm/customer/ref",data=json.dumps({'postCode':'M1015'}))
	# 	print(r.text)


	# def getInventory(self,Ilist):
	# 	r = self.s.post(self.base_url + "development-pc/v3/page/inventories",data=json.dumps(Ilist),headers=self.headers)
	# 	print(r.text)


	def add_saleOrder(self):
		r1 = self.s.post(self.base_url + "sales-pc/v3/pc/sale/saleOrders",data=json.dumps(test_sale.sale_data),headers=self.headers)
		sale_recordId = json.loads(r1.text)["data"]["recordId"]
		r2 = self.s.put(self.base_url + "sales-pc/v3/pc/sale/saleOrders/auditing/%s" %sale_recordId)
		print(r1.text)
		return sale_recordId


	def audit_saleOrder(self):
		'''
		审核通过销售订单
		执行时调用

		'''
		r1 = self.s.put(self.base_url + "sales-pc/v3/pc/sale/saleOrders/audited/%s"%self.add_saleOrder())
		sleep(1)
		return self


	def getBomId(self,Blist):
		sleep(1)
		r = self.s.post(self.base_url + "development-pc/v3/bom/page/list",data=json.dumps(Blist),headers=self.headers)
		print("BOM_ID：%s"%(json.loads(r.text)["data"]["content"][0]["bomId"]))
		return json.loads(r.text)["data"]["content"][0]["bomId"]


	def add_orderBom(self):
		bomId = self.getBomId(Blist)
		r = self.s.post(self.base_url + "development-pc/v3/bom/pending",params={"bomId":str(bomId)},headers=self.headers)
		return bomId


	def audit_orderBom(self):
		'''
		审核通过销售订单bom
		执行时调用
		
		'''
		r = self.s.post(self.base_url + "development-pc/v3/bom/audit",params={"bomId":str(self.add_orderBom())},headers=self.headers)		
		print(r.text)


	def Clear(self,cdata):
		'''
		清理账套数据
		'''
		r = self.s.post(self.base_url + "/warehouse-pc/v3/clear",params=cdata,headers=self.headers)
		print(r.text)




if __name__ == '__main__':
	login_esg = {'username':13928494604,'password':123456,'type':1}
	usercode = {'username':'___ierp_switch_usercode___819537415'}
	Blist = {"keyword":"","type":"ORDER","customerCode":"82145594","pageIndex":0,"pageSize":5000,"workFlowStatus":["PENDING_OPERATE","REJECT","PENDING_CHANGE"]}
	cdata = {"ip":"192.168.1.187","port":3306,"user":"yunji","pwd":"123456","auth":"1;2#4$5%6^7&8*qazwsxedc","flag":"true","entCode":"65362786"}
	for i in range(0,1):
		print('<<<<<第%s个订单>>>>>%s'%(i,'\n'))
		# TestYunJi().login(login_esg).switchAccount(usercode).audit_saleOrder().audit_orderBom()
		TestYunJi().login(login_esg).switchAccount(usercode).audit_saleOrder().audit_orderBom()



