from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, QEvent
from start_page import Ui_StartPage as start_form
from theatre import Ui_Form as drama_theatre
from repertoire import Ui_repertoire as repertoire
from play import Ui_play as play
from accepting import Ui_Accepting as accepting
from import_bd import Import_export
from PIL import Image
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import sqlite3
import sys


class Main_form(QMainWindow, start_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # настройка обработчиков событий
        self.nextPage.clicked.connect(self.next_page)
        self.previousPage.clicked.connect(self.previous_page)
        self.Dram_theatre_ok.clicked.connect(self.open_drama_theatre)
        self.Dram_theatre_ok.installEventFilter(self)
        self.nextPage.installEventFilter(self)
        self.previousPage.installEventFilter(self)

    def eventFilter(self, obj, event):
        # обработка наведения курсора мыши на кнопку
        if event.type() == QEvent.Enter and obj.isEnabled():
            # изменение стиля на выделенный
            obj.setStyleSheet('''background-color: #ff8a00;
                            border: 7px double #f7f7f7;
                            ''')
            # изменение стиля на невыделенный
        elif event.type() == QEvent.Leave:
            obj.setStyleSheet('''background-color: #f7f7f7;
                            border: 7px double #ff8a00;
                            ''')
        return QWidget.eventFilter(self, obj, event)

    def next_page(self):
        # переключение на след страницу
        self.stackedWidget.setCurrentIndex(
            self.stackedWidget.currentIndex() + 1)
        if self.stackedWidget.currentIndex() == 1:
            self.nextPage.setEnabled(False)
        self.previousPage.setEnabled(True)

    def previous_page(self):
        # переключение на пред страницу
        self.stackedWidget.setCurrentIndex(
            self.stackedWidget.currentIndex() - 1)
        if self.stackedWidget.currentIndex() == 0:
            self.previousPage.setEnabled(False)
        self.nextPage.setEnabled(True)

    def open_drama_theatre(self):
        # открытие репертуара
        # в аргументе указывается БД театра
        self.repertoire_form = Repertoire('theatre_test')
        self.repertoire_form.show()
        self.close()


class Repertoire(QWidget, repertoire):
    def __init__(self, data_base):
        super().__init__()
        self.setupUi(self)
        # импортирование БД
        self.data_base = data_base
        importer = Import_export()
        self.result = importer.import_table(data_base, 'repertoire')
        self.d = dict()
        self.last_line = ''
        # заполнение listWidget спектаклями
        for i in self.result:
            self.listWidget.addItem(i[1])
            self.d[i[1]] = i
        self.listWidget.itemDoubleClicked.connect(self.push)
        self.back_to_start.clicked.connect(self.push_back)
        self.rb_name.toggled.connect(self.start_search_by_name)
        self.rb_date.toggled.connect(self.start_search_by_date)
        self.search_by_name_timer = QTimer()  # таймер для поиска по имени
        self.search_by_name_timer.timeout.connect(self.search_by_name)
        self.search_by_date_timer = QTimer()  # таймер для поиска по дате
        self.search_by_date_timer.timeout.connect(self.search_by_date)
        self.back_to_start.installEventFilter(self)
        self.start_search_by_name()

    def eventFilter(self, obj, event):
        # обработка наведения курсора мыши на кнопку
        if event.type() == QEvent.Enter and obj.isEnabled():
            # изменение стиля на выделенный
            obj.setStyleSheet('''background-color: #ff8a00;
                            border: 7px double #f7f7f7;
                            ''')
            # изменение стиля на невыделенный
        elif event.type() == QEvent.Leave:
            obj.setStyleSheet('''background-color: #f7f7f7;
                            border: 7px double #ff8a00;
                            ''')
        return QWidget.eventFilter(self, obj, event)

    def push(self):
        self.search_by_name_timer.stop()
        con = sqlite3.connect('data/' + self.data_base + '.db')
        cursor = con.cursor()
        # получение всех спектаклей по времени
        tables = [i[1] for i in con.execute(
            "select * from sqlite_master where type = 'table'")]
        selected_item_ = self.listWidget.selectedItems()[0].text()
        self.selected = self.d[selected_item_]
        selected_item = ''
        # нахождение подходящих спектаклей
        for i in selected_item_.upper():
            if i in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                selected_item += i
        self.dates = [i for i in tables if selected_item.upper() in i]
        self.play_form = Play_form(self.selected, self.dates, self.data_base)
        self.play_form.show()
        self.close()

    def start_search_by_name(self):
        importer = Import_export()
        self.result = importer.import_table(self.data_base, 'repertoire')
        self.d = dict()
        self.last_line = ''
        # заполнение listWidget спектаклями
        for i in self.result:
            self.listWidget.addItem(i[1])
            self.d[i[1]] = i
        # запуск поиска по имени в реальном времени
        self.lineEdit.setEnabled(True)
        self.calendarWidget.setEnabled(False)
        self.last_line = self.lineEdit.text()
        self.search_by_name_timer.start(10)
        self.search_by_date_timer.stop()

    def start_search_by_date(self):
        self.lineEdit.setText('') 
        importer = Import_export()
        self.result = importer.import_table(self.data_base, 'repertoire')
        self.d = dict()
        self.last_line = ''
        # заполнение listWidget спектаклями
        for i in self.result:
            self.listWidget.addItem(i[1])
            self.d[i[1]] = i
        # запуск поиска по дате в реальном времени
        self.lineEdit.setEnabled(False)
        self.calendarWidget.setEnabled(True)
        self.last_date = self.calendarWidget.selectedDate()
        self.last_date = self.last_date.toString('dd.MM.yyyy')
        self.search_by_date_timer.start(10)
        self.search_by_name_timer.stop()

    def search_by_name(self):
        # поиск по имени в реальном времени
        if not self.lineEdit.text() and self.lineEdit.text() != self.last_line:
            self.listWidget.clear()
            self.d = dict()
            for i in self.result:
                self.listWidget.addItem(i[1])
                self.d[i[1]] = i
            self.last_line = self.lineEdit.text()
        else:
            if self.last_line != self.lineEdit.text():
                self.listWidget.clear()
                self.d = dict()
                for i in self.result:
                    if i[1].lower().find(self.lineEdit.text().lower()) == 0:
                        self.listWidget.addItem(i[1])
                        self.d[i[1]] = i
                self.last_line = self.lineEdit.text()

    def search_by_date(self):
        # поиск по дате в реальном времени
        date = self.calendarWidget.selectedDate()
        date = date.toString('dd.MM.yyyy')
        if self.last_date != date:
            self.listWidget.clear()
            self.d = dict()
            con = sqlite3.connect('data/' + self.data_base + '.db')
            cursor = con.cursor()
            tables = [i[1] for i in con.execute(
                "select * from sqlite_master where type = 'table'")]
            for i in tables:
                if date.replace('.', '') in i:
                    for j in self.result:
                        if j[1].lower().replace(' ', '') in i.lower():
                            self.listWidget.addItem(j[1])
                            self.d[j[1]] = j
        self.last_date = date

    def push_back(self):
        # возвращение на пред форму
        wnd.show()
        self.close()


class Play_form(QWidget, play):
    def __init__(self, selected, dates, data_base):
        super().__init__()
        self.setupUi(self)
        self.data_base = data_base
        # импортирование картинки из БД
        with open('picture.jpg', 'wb') as f:
            f.write(selected[4])
        first_img = Image.open('picture.jpg')
        # выставление размера изображения
        new_img = first_img.resize((771, 251))
        new_img.save('picture.jpg')
        self.label.setPixmap(QPixmap('picture.jpg'))
        # запись всех доступных дат в ListWidget
        for i in dates:
            item = i[-12:]
            item = item[:2] + '.' + item[2:4] + '.' + \
                item[4:8] + ' ' + item[8:10] + ':' + item[10:]
            self.listWidget.addItem(item)
        self.director.setText(selected[3])  # импортирование режиссера
        self.author.setText(selected[6])  # импортирование автора
        self.plainTextEdit.setPlainText(selected[2])  # импортирование описания
        self.setWindowTitle(selected[1])
        self.name.setText(selected[1])  # импортирование названия
        global play_name
        play_name = selected[1]
        self.listWidget.itemDoubleClicked.connect(self.push)
        self.back.clicked.connect(self.push_back)
        self.back.installEventFilter(self)

    def eventFilter(self, obj, event):
        # обработка наведения курсора мыши на кнопку
        if event.type() == QEvent.Enter and obj.isEnabled():
            # изменение стиля на выделенный
            obj.setStyleSheet('''background-color: #ff8a00;
                            border: 7px double #f7f7f7;
                            ''')
            # изменение стиля на невыделенный
        elif event.type() == QEvent.Leave:
            obj.setStyleSheet('''background-color: #f7f7f7;
                            border: 7px double #ff8a00;
                            ''')
        return QWidget.eventFilter(self, obj, event)

    def push(self):
        global gl_theatre
        con = sqlite3.connect('data/' + self.data_base + '.db')
        cursor = con.cursor()
        tables = [i[1] for i in con.execute(
            "select * from sqlite_master where type = 'table'")]
        selected_item = self.listWidget.selectedItems()[0].text()
        selected_item = selected_item.replace(
            '.', '').replace(' ', '').replace(':', '')
        # нахождение подходящей таблицы со спектаклем
        for i in tables:
            if selected_item in i:
                if self.data_base == 'theatre_test':
                    self.theatre = Drama_theatre_form(self.data_base, i)
                    gl_theatre = self.theatre
                    self.theatre.showFullScreen()

    def push_back(self):
        # возвращение на пред форму
        self.repertoire = Repertoire(self.data_base)
        self.repertoire.show()
        self.close()


class Drama_theatre_form(QWidget, drama_theatre):
    def __init__(self, data_base, i):
        super().__init__()
        self.setupUi(self)
        importer = Import_export()
        result = importer.import_table(data_base, i)
        self.chosen = []
        self.data_base = data_base
        self.table = i
        self.back.clicked.connect(self.push_back)
        self.Accept.clicked.connect(self.push_accept)
        for i in range(len(result)):
            if result[i][3] == 0:
                self.buttons[i].setEnabled(False)
            else:
                # изменение цвета кнопки в зависимости от ее цены
                self.buttons[i].setToolTip(
                    result[i][1] + ' место ' +
                    str(result[i][2]) + '\n(' + str(result[i][3]) + ' руб.)')
                if result[i][3] == 900:
                    self.buttons[i].setStyleSheet(
                        'background-color: rgb(200, 0, 0)')
                elif result[i][3] == 800:
                    self.buttons[i].setStyleSheet(
                        'background-color: rgb(255, 170, 0)')
                elif result[i][3] == 700:
                    self.buttons[i].setStyleSheet(
                        'background-color: rgb(255, 255, 0)')
                elif result[i][3] == 600:
                    self.buttons[i].setStyleSheet(
                        'background-color: rgb(85, 255, 0)')
                elif result[i][3] == 500:
                    self.buttons[i].setStyleSheet(
                        'background-color: rgb(85, 255, 255)')
                elif result[i][3] == 400:
                    self.buttons[i].setStyleSheet(
                        'background-color: rgb(85, 85, 255)')
                elif result[i][3] == 300:
                    self.buttons[i].setStyleSheet(
                        'background-color: rgb(85, 0, 127)')
                elif result[i][3] == 200:
                    self.buttons[i].setStyleSheet(
                        'background-color: rgb(31, 135, 75)')
            self.buttons[i].clicked.connect(self.push)
        self.back.installEventFilter(self)
        self.Accept.installEventFilter(self)

    def eventFilter(self, obj, event):
        # обработка наведения курсора мыши на кнопку
        if event.type() == QEvent.Enter and obj.isEnabled():
            # изменение стиля на выделенный
            obj.setStyleSheet('''background-color: #ff8a00;
                            border: 7px double #f7f7f7;
                            ''')
            # изменение стиля на невыделенный
        elif event.type() == QEvent.Leave:
            obj.setStyleSheet('''background-color: #f7f7f7;
                            border: 7px double #ff8a00;
                            ''')
        return QWidget.eventFilter(self, obj, event)

    def push(self):
        btn = self.sender()
        # проверка на выбранность
        if btn.styleSheet() != 'background-color: rgb(72, 72, 72)':
            btn.setStyleSheet('background-color: rgb(72, 72, 72)')
            self.chosen.append(btn)
            self.Accept.setEnabled(True)
        else:
            # изменение цвета кнопки в зависимости от ее цены
            if '900 руб.' in btn.toolTip():
                btn.setStyleSheet('background-color: rgb(200, 0, 0)')
            elif '800 руб.' in btn.toolTip():
                btn.setStyleSheet('background-color: rgb(255, 170, 0)')
            elif '700 руб.' in btn.toolTip():
                btn.setStyleSheet('background-color: rgb(255, 255, 0)')
            elif '600 руб.' in btn.toolTip():
                btn.setStyleSheet('background-color: rgb(85, 255, 0)')
            elif '500 руб.' in btn.toolTip():
                btn.setStyleSheet('background-color: rgb(85, 255, 255)')
            elif '400 руб.' in btn.toolTip():
                btn.setStyleSheet('background-color: rgb(85, 85, 255)')
            elif '300 руб.' in btn.toolTip():
                btn.setStyleSheet('background-color: rgb(85, 0, 127)')
            elif '200 руб.' in btn.toolTip():
                btn.setStyleSheet('background-color: rgb(31, 135, 75)')
            self.chosen.remove(btn)  # отжатие кнопки
            if not self.chosen:
                self.Accept.setEnabled(False)

    def push_back(self):
        # возвращение на пред форму
        self.close()

    def push_accept(self):
        # переход на форму подтверждения покупки
        # в качестве одного из аргументов передается название театра
        self.accept = Accepting_form(
            self.chosen, 'drama', self.data_base, self.table)
        self.accept.show()


class Accepting_form(QWidget, accepting):
    def __init__(self, chosen, theatre, data_base, table):
        super().__init__()
        self.setupUi(self)
        self.chosen = chosen
        self.data_base = data_base
        self.table = table
        if theatre == 'drama':
            # определение расположения выбранных мест в зависимости от их цены
            bal_right = set(range(68, 81))
            bal_left = set(range(105, 117))
            amf_right = set(range(146, 153)) | set(range(172, 186))
            amf_left = set(range(165, 172)) | set(range(210, 224))
            bel_right = set(range(264, 268)) | set(range(296, 305)) | set(
                range(336, 349)) | set(range(382, 395))
            bel_left = set(range(292, 296)) | set(range(327, 335)) | set(
                range(369, 382)) | set(range(413, 426))
            ben_right = {548, 549, 578, 579, 606, 607, 634, 635,
                         662, 663, 690, 691, 718, 719, 746, 747, 774}
            ben_left = {576, 577, 604, 605, 632, 633, 660, 661,
                        688, 689, 716, 717, 744, 745, 772, 773, 795}
            for i in self.chosen:
                if (int(i.objectName()[1:]) <= 117
                        and int(i.objectName()[1:]) not in (bal_left | bal_right)):
                    self.listWidget.addItem(
                        'Балкон ' + i.toolTip().replace('\n', ' ').lower())
                elif (int(i.objectName()[1:]) >= 118
                      and int(i.objectName()[1:]) <= 223
                      and int(i.objectName()[1:]) not in (amf_left | amf_right)):
                    self.listWidget.addItem(
                        'Амфитеатр ' + i.toolTip().replace('\n', ' ').lower())
                elif (int(i.objectName()[1:]) >= 224
                      and int(i.objectName()[1:]) <= 425
                      and int(i.objectName()[1:]) not in (bel_left | bel_right)):
                    self.listWidget.addItem(
                        'Бельэтаж ' + i.toolTip().replace('\n', ' ').lower())
                elif (int(i.objectName()[1:]) >= 426
                      and int(i.objectName()[1:]) <= 815
                      and int(i.objectName()[1:]) not in (ben_left | ben_right)):
                    self.listWidget.addItem(
                        'Партер ' + i.toolTip().replace('\n', ' ').lower())
                elif int(i.objectName()[1:]) in bal_right:
                    self.listWidget.addItem(
                        'Балкон правая сторона ' +
                        i.toolTip().replace('\n', ' ').lower())
                elif int(i.objectName()[1:]) in bal_left:
                    self.listWidget.addItem(
                        'Балкон левая сторона ' +
                        i.toolTip().replace('\n', ' ').lower())
                elif int(i.objectName()[1:]) in amf_right:
                    self.listWidget.addItem(
                        'Амфитеатр правая сторона ' +
                        i.toolTip().replace('\n', ' ').lower())
                elif int(i.objectName()[1:]) in amf_left:
                    self.listWidget.addItem(
                        'Амфитеатр левая сторона ' +
                        i.toolTip().replace('\n', ' ').lower())
                elif int(i.objectName()[1:]) in bel_right:
                    self.listWidget.addItem(
                        'Бельэтаж правая сторона ' +
                        i.toolTip().replace('\n', ' ').lower())
                elif int(i.objectName()[1:]) in bel_left:
                    self.listWidget.addItem(
                        'Бельэтаж левая сторона ' +
                        i.toolTip().replace('\n', ' ').lower())
                elif int(i.objectName()[1:]) in ben_right:
                    self.listWidget.addItem(
                        'Ложа бенуар правая ' +
                        i.toolTip().replace('\n', ' ').lower())
                elif int(i.objectName()[1:]) in ben_left:
                    self.listWidget.addItem(
                        'Ложа бенуар левая ' +
                        i.toolTip().replace('\n', ' ').lower())
        self.cancel.clicked.connect(lambda x: self.close())
        self.Accept.clicked.connect(self.push)
        self.lineEdit.returnPressed.connect(self.Accept.click)
        self.cancel.installEventFilter(self)
        self.Accept.installEventFilter(self)

    def eventFilter(self, obj, event):
        # обработка наведения курсора мыши на кнопку
        if event.type() == QEvent.Enter and obj.isEnabled():
            # изменение стиля на выделенный
            obj.setStyleSheet('''background-color: #ff8a00;
                            border: 7px double #f7f7f7;
                            ''')
            # изменение стиля на невыделенный
        elif event.type() == QEvent.Leave:
            obj.setStyleSheet('''background-color: #f7f7f7;
                            border: 7px double #ff8a00;
                            ''')
        return QWidget.eventFilter(self, obj, event)

    def push(self):
        # Отправка email
        global play_name
        global gl_theatre
        if '@' not in self.lineEdit.text() or '.' not in self.lineEdit.text():
            self.label_2.setText('Неверный формат email')
        else:
            import random
            n = str(random.randint(1, 99999))
            text = play_name + '\nНомер заказа:' + n + '\nВаши билеты:\n'
            n = self.listWidget.count()
            for j in [str(self.listWidget.item(i).text()) for i in range(n)]:
                text += j + '\n'
            text += 'Спасибо за покупку!'

            smtp_host = 'smtp.yandex.ru'
            login, password = 'tickets.theatre@yandex.ru', 'password_to_app'

            msg = MIMEText(text, 'plain', 'utf-8')
            msg['Subject'] = Header('Покупка билетов', 'utf-8')
            msg['From'] = login
            msg['To'] = ", ".join(self.lineEdit.text())

            sender = smtplib.SMTP(smtp_host, 587)
            sender.set_debuglevel(1)
            sender.starttls()
            sender.login(login, password)
            try:
                sender.sendmail(
                    msg['From'], self.lineEdit.text(), msg.as_string())
                self.label_2.setText('')
                gl_theatre.close()
                self.close()
                sender.quit()
                exporter = Import_export()
                for i in self.chosen:
                    exporter.update_table(self.data_base, self.table, "UPDATE " +
                                        self.table + " SET price = 0 WHERE id = "
                                        + i.objectName()[1:])
            except:
                self.label_2.setText('Произошла ошибка')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Main_form()
    play_name = ''
    gl_theatre = None
    wnd.show()
    sys.exit(app.exec())
