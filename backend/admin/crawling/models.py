import pandas as pd
from sklearn import preprocessing
from admin.common.models import ValueObject, Printer, Reader
from icecream import ic
import numpy as np
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
class Crawling(object):
    def __init__(self):
        pass

    def process(self):
        vo = ValueObject()
        vo.context = 'admin/crawling/data/'
        vo.url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
        driver = webdriver.Chrome(f'{vo.context}/chromedriver')
        driver.get(vo.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div', {'class': 'tit3'})
        arr = [div.a.string for div in all_div]
        for i in arr:
            print(i)
        dt = {i+1 : val for i, val in enumerate(arr)}
        with open(vo.context+'with_save.csv', 'w', encoding='UTF-8') as f:
            w = csv.writer(f)
            w.writerow(dt.keys())
            w.writerow(dt.values())
        driver.close()

