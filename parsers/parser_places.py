from selenium import webdriver
import requests
import urllib.request
from import_bd import Import_export
import sqlite3


class Parcer_places:
    def __init__(self, url):
        self.prices = {'pricezone-510 m-available': 200, 
        'pricezone-509 m-available': 400, 
        'pricezone-508 m-available': 500,
        'pricezone-507 m-available': 600,
        'pricezone-506 m-available': 700,
        'pricezone-505 m-available': 800,
        'pricezone-504 m-available': 900,
        None: 0}
        self.url = url
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=options)
    
    def parc(self):
        self.driver.get(self.url)
        cols = self.driver.find_elements_by_tag_name('tr')
        balcon_tr = cols[2:7] #tr
        amf_tr = cols[8:11]
        bal_tr = cols[12:18]
        part_tr = cols[19:24]
        ben_tr = cols[25:35] #бенуар
        balcon = []
        for i in balcon_tr:
            for j in i.find_elements_by_tag_name('td'):
                if j.get_attribute('class') != 'row-item' and j.get_attribute('class') != 'label' and j.get_attribute('colspan') == None:
                    if not j.get_attribute('class'):
                        cl = self.prices[None]
                    else:
                        cl = self.prices[j.get_attribute('class')]
                    balcon.append((i.get_attribute('name'), j.text, cl))
        amf = []
        for i in amf_tr:
            for j in i.find_elements_by_tag_name('td'):
                if j.get_attribute('class') != 'row-item' and j.get_attribute('class') != 'label' and j.text != ' ':
                    if not j.get_attribute('class'):
                        cl = self.prices[None]
                    else:
                        cl = self.prices[j.get_attribute('class')]
                    amf.append((i.get_attribute('name'), j.text, cl))
        bal = []
        for i in bal_tr:
            for j in i.find_elements_by_tag_name('td'):
                if j.get_attribute('class') != 'row-item' and j.get_attribute('class') != 'label' and j.text != ' ':
                    if not j.get_attribute('class'):
                        cl = self.prices[None]
                    else:
                        cl = self.prices[j.get_attribute('class')]
                    bal.append((i.get_attribute('name'), j.text, cl))
        part = []
        for i in part_tr:
            for j in i.find_elements_by_tag_name('td'):
                if j.get_attribute('class') != 'row-item' and j.get_attribute('class') != 'label' and j.text != ' ':
                    if not j.get_attribute('class'):
                        cl = self.prices[None]
                    else:
                        cl = self.prices[j.get_attribute('class')]
                    part.append((i.get_attribute('name'), j.text, cl))
        ben = []
        for i in ben_tr:
            for j in i.find_elements_by_tag_name('td'):
                if j.get_attribute('class') != 'row-item' and j.get_attribute('class') != 'label' and j.text != ' ':
                    if not j.get_attribute('class'):
                        cl = self.prices[None]
                    else:
                        cl = self.prices[j.get_attribute('class')]
                    ben.append([i.get_attribute('name'), j.text, cl])
        result = balcon + amf + bal + part + ben
        self.driver.quit()
        return result