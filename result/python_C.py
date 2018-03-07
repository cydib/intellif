#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-06 16:35:31
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import unittest,HTMLTestRunner



class Test(unittest.TestCase):


	def setUp(self):
		print("<<<<<< start test >>>>>>")
		self.a = 5
		self.b = 11

	def tearDown(self):
		print("<<<<<< end test >>>>>>")

	def test1(self):
		print(self.a + self.b)

	def test2(self):
		self.assertEqual(self.a,self.b)

if __name__ == '__main__':
	suit=unittest.TestSuite()
	suit.addTest(Test("test1"))
	suit.addTest(Test("test2"))
	fp = open('./result.html','wb')
	runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                          title=u'<test demo>test report',
                                          description=u'describe: ... ')
	runner.run(suit)
	fp.close()
	