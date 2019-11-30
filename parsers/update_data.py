from bs4 import BeautifulSoup
import requests
from parser_places import Parser_places
from import_bd import Import_export

class Updater:
    def __init__(self, url):
        r = requests.get(url)
        self.soup = BeautifulSoup(r.text)
        self.url = url

    def update(self):
        months = {'января': '01', 'февраля': '02',
        'марта': '03', 'апреля': '04', 'мая': '05', 
        'июня': '06', 'июля': '07', 'августа': '08', 
        'сентября': '09', 'октября': '10', 
        'ноября': '11', 'декабря': '12'}
        events = self.soup.find_all('tr')[1:]
        for i in events[13:]:
            link = i.find_all('td')[-1].find('a').get('href')
            date_ = i.find_all('td')[1].getText().split()
            name = i.find_all('td')[0].getText().split()[:-1]
            if i.find_all('td')[2].getText() != 'Камерный зал -САТД':
                date = date_[1] + months[date_[2]] + date_[3] + date_[4].split(':')[0] + date_[4].split(':')[1]
                parcer = Parcer_places(self.url[:-1] + link)
                result = parcer.parc()
                table = ''.join(name) + date
                table = table.replace('.', '')
                table = table.replace('-', '')
                table = table.replace(',', '')
                if table[0]  in '0123456789':
                    table = 'a' + table
                print(table)
                q = """CREATE TABLE """ + table + """ 
                    (col, row, price)"""
                exporter = Import_export
                exporter.create_table('theatre_test', q)
                try:
                    for j in result:
                        exporter.export_table('theatre_test', table, 'INSERT INTO ' + table + ' VALUES (?, ?, ?)', j)
                    print('SUCCESS')
                except:
                    print(name)

u = Updater('http://ticket.dramtheatre.ru/')
u.update()

            
