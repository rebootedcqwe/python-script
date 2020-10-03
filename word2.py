#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version  : Python 3.7.3
# @Time     : 2019/7/24 20:13

import xlrd
import time
import csv

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')    # 设置无界面
options.add_argument('--no-sandbox')  # root用户下运行代码需添加这一行

browser = webdriver.Chrome(options=options)
url = "https://fanyi.baidu.com/?aldtype=85#en/zh/"

browser.get(url)
WebDriverWait(browser, 1000).until(EC.presence_of_all_elements_located((By.ID, 'baidu_translate_input')))

excelfile = xlrd.open_workbook(r'/root/aaa.xlsx')
sheet = excelfile.sheet_by_name("单词")
#sheet = excelfile.sheet_by_name("aaa")
cnt = sheet.nrows

with open(r'/root/result.csv', 'a', encoding='utf-8',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(("单词", "音标", "注释"))

for i in range(cnt):
    mystr = sheet.cell(i, 0).value
    browser.find_element_by_id('baidu_translate_input').send_keys(mystr)
    browser.find_element_by_id('translate-button').click()
    WebDriverWait(browser, 1000).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'trans-left')))
    try:
        words = browser.find_element_by_class_name('strong').text  # 单词
        phonetic = browser.find_element_by_class_name('dictionary-spell').text  # 音标
        comment = browser.find_element_by_class_name('dictionary-comment').text  # 音标
        print("%s   %s   %s" % (words, phonetic, comment))

        data = (words, phonetic, comment)
        with open(r'/root/result.csv', 'a', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
    except:
        pass

    time.sleep(1)
    browser.find_element_by_id('baidu_translate_input').clear()

browser.close()
browser.quit()
print("完成，请到相应文件夹查看！")
