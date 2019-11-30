from bs4 import BeautifulSoup
import requests
from import_bd import Import_export
import urllib.request


class Parcer_repertoire:
    def __init__(self):
        url = "http://www.dramtheatre.ru/repertoire/" #указываем url адрес
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        play_length = len(soup.find('ul', {'class': 'pagination'}).find_all('li')) - 1 #узнаем кол-во страниц на сайте
        play_list = [] #список всех спектаклей
        for i in range(2, 2 + play_length):
            url = 'http://www.dramtheatre.ru/repertoire/?PAGEN_1=' + str(i) #url страницы
            r = requests.get(url)
            soup = BeautifulSoup(r.text)
            a = list(soup.find_all('div', {'class':'afisha__caption'}))
            play_list += a

        exporter = Import_export()
        k = 0
        for i in play_list:
            name = i.find('a').getText()
            link = 'http://www.dramtheatre.ru' + i.find('a').get('href') #url отдельного спектакля
            r = requests.get(link)
            soup = BeautifulSoup(r.text)
            details = [j.find('dd').getText() for j in list(soup.find_all('dl', {'class': 'event__details'}))[:3]] #автор, длительность представления, режиссер
            if details: #если нашлись
                datetime = soup.find('div', {'class': 'event__sidebar'})
                date = list(datetime.find_all('div', {'class': 'event__date'}))
                time = list(datetime.find_all('div', {'class': 'event__time'}))
                datetime = list(zip([j.getText() for j in date], [j.getText() for j in time])) #дата и время   
                about = soup.find('div', {'class': 'event__content'}).find('p').getText() #описание
                image = soup.find('div', {'class': 'event'}).find('header', {'class': 'event__header'}).find('img').get('src') #фотография
                urllib.request.urlretrieve('http://www.dramtheatre.ru' + image, 'test.jpg') #скачиваем фотографию и записываем во временный файл
                for j in details: # корректируем переменные при отсутствии данных
                    if set('0123456789') & set(j):
                        length = j
                        details.remove(length)
                        break
                author = details[0] # автор
                try:
                    director = details[1] # режиссер
                except:
                    pass
                time_result = ';'.join([','.join(item) for item in datetime]) # дата и время для записи в БД
                with open('test.jpg', 'rb') as img:
                    img_bin = img.read()
                    result = [k, name, about, director, img_bin, time_result, author]
                exporter.export_table('theatre_test', 'drama_theatre_repertoire', 'INSERT INTO drama_theatre_repertoire VALUES (?, ?, ?, ?, ?, ?, ?)', result) # запись в БД
                k += 1
