#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-03 12:29:02
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import requests, time
from bs4 import BeautifulSoup


def getData():
    base_url = "https://www.v2ex.com/?tab=deals"
    r = requests.get(base_url).text
    soup = BeautifulSoup(r, "html.parser")

    num = 0
    for i in soup.find_all("span", class_="item_title"):
        num += 1
        for j in i:
            print("第%s帖,标题：%s,链接：%s" % (num, j.get_text(), "https://www.v2ex.com" + j['href']))


if __name__ == '__main__':
    s = 0
    while (True):
        s += 1
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        print("%s<<<<<<<<<<<<<<<%s 第%s次查询 >>>>>>>>>>>>>>>>>%s" % ('\n',now,s,'\n'))
        getData()
        time.sleep(600)
