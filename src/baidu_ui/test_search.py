# -*-coding:GBK -*-
import pytest
from .const import *
import xlrd
from selenium import webdriver
from time import sleep, ctime



class Test_baidu_search():
    def test_search_excel(self):
        driver = webdriver.Chrome()
        tableopen = xlrd.open_workbook(Excel_Dir)
        count = len(tableopen.sheets())
        table = tableopen.sheet_by_name('Sheet1')
        # height = table.nrows
        height = table.col_values(0)
        driver.get("https://www.baidu.com/")
        for i in height:
            driver.find_element_by_id("kw").clear()
            driver.find_element_by_id("kw").send_keys(str(i))
            driver.find_element_by_id("su").click()
            sleep(2)
        driver.quit()

    def test_s(self):
        print("11111111111111")
        assert 1 == 1

    def test_f(self):
        print("22222222222222")
        assert 1 == 0
