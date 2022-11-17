import sys
import json
import random
import shutil
import os.path
import os
import sqlite3

from gfx.table import Table
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton
from gfx.main_des import Ui_MainWindow
from gfx.rez import rez
from gfx.Opros import Opros
from gfx.settings_opros import Set_opros
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


with open('files/Quotes.json', 'r') as t:
    quotes = json.load(t)


if os.path.exists('Cashe'):
    pass
else:
    os.mkdir("Cashe")


if os.path.exists('Cashe/Data_Cashe.sqlite3'):
    pass
else:
    shutil.copyfile('files/Data.sqlite3', 'Cashe/Data_Cashe.sqlite3')


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textBrowser.setText(f'{quotes[str(random.randint(1, 100))][1]} - {quotes[str(random.randint(1, 100))][0]}')
        self.pushButton_3.clicked.connect(self.quotes)
        self.pushButton.clicked.connect(self.start)
        self._createMenuBar()
    
    def _createMenuBar(self):
        exitAction = QAction(QIcon('gfx/help.svg'), 'Help', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Help')
        exitAction.triggered.connect(self.Clik_Help)
        menuBar = self.menuBar()
        toolbar = self.addToolBar('Help')
        toolbar.addAction(exitAction)

    def quotes(self):
        a = random.randint(1, 100)
        b = (f'{quotes[str(a)][1]} - {quotes[str(a)][0]}')
        self.textBrowser.setText(b)

    def start(self):
        self.start = Setings_opros()
        self.start.show()
        self.close()

    def Clik_Help(self):
        os.startfile('ReadMe.md')


class Setings_opros(QMainWindow, Set_opros):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click_close)
        self.pushButton_2.clicked.connect(self.click_ok)
        self.spinBox.setMinimum(2)
        con = sqlite3.connect('cashe/Data_Cashe.sqlite3')
        cur = con.cursor()
        result = cur.execute("""SELECT COUNT(1) FROM Data_baze""").fetchall()
        con.close()
        self.spinBox.setMaximum(result[0][0])
        self.spinBox.valueChanged.connect(self.show_result)
        #self.pushButton_3.clicked.connect(self.red)

    def red(self):
        self.start = Table()
        self.start.show()
        self.close()

    def show_result(self):
        self.value = self.spinBox.value()

    def click_ok(self):
        gggg = self.value
        self.start = Opros(self.spinBox.value())
        self.start.show()
        self.close()

    def click_close(self):
        self.start = MyWidget()
        self.start.show()
        self.close()


class Opros(QMainWindow, Opros):
    def __init__(self, lenn):
        super().__init__()
        self.setupUi(self)
        self.lenn = lenn
        self.num = 1
        self.prav = 0
        self.prav_button = random.randint(2, 4)
        con = sqlite3.connect('cashe/Data_Cashe.sqlite3')
        cur = con.cursor()
        result = cur.execute("""SELECT COUNT(1) FROM Data_baze""").fetchall()
        self.a = random.randint(1, result[0][0])
        zap = cur.execute(f"""
        SELECT ID={self.a},
            Data,
            Name,
            Prom
        FROM Data_baze;
        """).fetchall()
        ranotv = cur.execute(f"""
        SELECT Prom={zap[self.a][3]},
            Name
        FROM Data_baze;
        """).fetchall()
        con.close()
        ggg = 0
        rezult = []
        for i in ranotv:
            if i[0] == 1:
                rezult.append(i)
        self.textBrowser.setText(str(zap[self.a][1]))
        random.shuffle(rezult)
        if self.prav_button == 2:
            self.pushButton_2.setText(str(zap[self.a][2]))
            random.shuffle(rezult)
            self.pushButton_3.setText(rezult[0][1])
            rezult.pop(0)
            random.shuffle(rezult)
            self.pushButton_4.setText(rezult[0][1])
        elif self.prav_button == 3:
            self.pushButton_3.setText(str(zap[self.a][2]))
            random.shuffle(rezult)
            self.pushButton_2.setText(rezult[0][1])
            rezult.pop(0)
            random.shuffle(rezult)
            self.pushButton_4.setText(rezult[0][1])
        elif self.prav_button == 4:
            self.pushButton_4.setText(str(zap[self.a][2]))
            random.shuffle(rezult)
            self.pushButton_3.setText(rezult[0][1])
            rezult.pop(0)
            random.shuffle(rezult)
            self.pushButton_2.setText(rezult[0][1])

        self.pushButton_2.clicked.connect(self.prov2)
        self.pushButton_3.clicked.connect(self.prov3)
        self.pushButton_4.clicked.connect(self.prov4)

    def prov2(self):
        if self.prav_button == 2:
            self.prav += 1
        if self.num == self.lenn:
            self.start = rez(self.prav, self.lenn)
            self.start.show()
            self.close()
        else:
            self.num += 1
            self.prav_button = random.randint(2, 4)
            con = sqlite3.connect('cashe/Data_Cashe.sqlite3')
            cur = con.cursor()
            result = cur.execute("""SELECT COUNT(1) FROM Data_baze""").fetchall()
            self.a = random.randint(1, result[0][0])
            zap = cur.execute(f"""
            SELECT ID={self.a},
                Data,
                Name,
                Prom
            FROM Data_baze;
            """).fetchall()
            ranotv = cur.execute(f"""
            SELECT Prom={zap[self.a][3]},
                Name
            FROM Data_baze;
            """).fetchall()
            con.close()
            rezult = []
            for i in ranotv:
                if i[0] == 1:
                    rezult.append(i)
            self.textBrowser.setText(str(zap[self.a][1]))
            random.shuffle(rezult)
            if self.prav_button == 2:
                self.pushButton_2.setText(str(zap[self.a][2]))
                random.shuffle(rezult)
                self.pushButton_3.setText(rezult[0][1])
                rezult.pop(0)
                b = random.randint(0, len(rezult)-1)
                self.pushButton_4.setText(rezult[0][1])
            elif self.prav_button == 3:
                self.pushButton_3.setText(str(zap[self.a][2]))
                random.shuffle(rezult)
                self.pushButton_2.setText(rezult[0][1])
                rezult.pop(0)
                random.shuffle(rezult)
                self.pushButton_4.setText(rezult[0][1])
            elif self.prav_button == 4:
                self.pushButton_4.setText(str(zap[self.a][2]))
                random.shuffle(rezult)
                self.pushButton_3.setText(rezult[0][1])
                rezult.pop(0)
                random.shuffle(rezult)
                self.pushButton_2.setText(rezult[0][1])

    def prov3(self):
        if self.prav_button == 3:
            self.prav += 1
        if self.num == self.lenn:
            self.start = rez(self.prav, self.lenn)
            self.start.show()
            self.close()
        else:
            self.num += 1
            self.prav_button = random.randint(2, 4)
            con = sqlite3.connect('cashe/Data_Cashe.sqlite3')
            cur = con.cursor()
            result = cur.execute("""SELECT COUNT(1) FROM Data_baze""").fetchall()
            self.a = random.randint(1, result[0][0])
            zap = cur.execute(f"""
            SELECT ID={self.a},
                Data,
                Name,
                Prom
            FROM Data_baze;
            """).fetchall()
            ranotv = cur.execute(f"""
            SELECT Prom={zap[self.a][3]},
                Name
            FROM Data_baze;
            """).fetchall()
            con.close()
            ggg = 0
            rezult = []
            for i in ranotv:
                if i[0] == 1:
                    rezult.append(i)
            self.textBrowser.setText(str(zap[self.a][1]))
            random.shuffle(rezult)
            if self.prav_button == 2:
                self.pushButton_2.setText(str(zap[self.a][2]))
                random.shuffle(rezult)
                self.pushButton_3.setText(rezult[0][1])
                rezult.pop(0)
                b = random.randint(0, len(rezult)-1)
                self.pushButton_4.setText(rezult[0][1])
            elif self.prav_button == 3:
                self.pushButton_3.setText(str(zap[self.a][2]))
                random.shuffle(rezult)
                self.pushButton_2.setText(rezult[0][1])
                rezult.pop(0)
                random.shuffle(rezult)
                self.pushButton_4.setText(rezult[0][1])
            elif self.prav_button == 4:
                self.pushButton_4.setText(str(zap[self.a][2]))
                random.shuffle(rezult)
                self.pushButton_3.setText(rezult[0][1])
                rezult.pop(0)
                random.shuffle(rezult)
                self.pushButton_2.setText(rezult[0][1])

    def prov4(self):
        if self.prav_button == 4:
            self.prav += 1
        if self.num == self.lenn:
            self.start = rez(self.prav, self.lenn)
            self.start.show()
            self.close()
        else:
            self.num += 1
            self.prav_button = random.randint(2, 4)
            con = sqlite3.connect('cashe/Data_Cashe.sqlite3')
            cur = con.cursor()
            result = cur.execute("""SELECT COUNT(1) FROM Data_baze""").fetchall()
            self.a = random.randint(1, result[0][0])
            zap = cur.execute(f"""
            SELECT ID={self.a},
                Data,
                Name,
                Prom
            FROM Data_baze;
            """).fetchall()
            ranotv = cur.execute(f"""
            SELECT Prom={zap[self.a][3]},
                Name
            FROM Data_baze;
            """).fetchall()
            con.close()
            ggg = 0
            rezult = []
            for i in ranotv:
                if i[0] == 1:
                    rezult.append(i)
            self.textBrowser.setText(str(zap[self.a][1]))
            random.shuffle(rezult)
            if self.prav_button == 2:
                self.pushButton_2.setText(str(zap[self.a][2]))
                random.shuffle(rezult)
                self.pushButton_3.setText(rezult[0][1])
                rezult.pop(0)
                b = random.randint(0, len(rezult)-1)
                self.pushButton_4.setText(rezult[0][1])
            elif self.prav_button == 3:
                self.pushButton_3.setText(str(zap[self.a][2]))
                random.shuffle(rezult)
                self.pushButton_2.setText(rezult[0][1])
                rezult.pop(0)
                random.shuffle(rezult)
                self.pushButton_4.setText(rezult[0][1])
            elif self.prav_button == 4:
                self.pushButton_4.setText(str(zap[self.a][2]))
                random.shuffle(rezult)
                self.pushButton_3.setText(rezult[0][1])
                rezult.pop(0)
                random.shuffle(rezult)
                self.pushButton_2.setText(rezult[0][1])


class rez(QMainWindow, rez):
    def __init__(self, prav, len):
        super().__init__()
        self.setupUi(self)
        b = f"""
        Количество правильных ответов: {prav} из {len}
        Количество неправильных ответов: {len - prav} из {len}
        """
        self.label.setText(b)
        self.pushButton.clicked.connect(self.click)

    def click(self):
        self.start = MyWidget()
        self.start.show()
        self.close()


class Table(QMainWindow, Table):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("cashe\data_cashe.sqlite")
        self.pushButton.clicked.connect(self.update_result)
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.pushButton_2.clicked.connect(self.save_results)
        self.modified = {}
        self.titles = None

    def update_result(self):
        con = sqlite3.connect('cashe/Data_Cashe.sqlite3')
        cur = self.con.cursor()
        result = cur.execute("""SELECT ID,
            Data,
            Name,
            Prom
        FROM Data_baze;
        """).fetchall()
        self.tableWidget.setRowCount(len(result))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def delete_elem(self):
        answer, ok_pressed = QInputDialog.getItem(
        self, "Подтверждение удаления",
        "Вы точно хотите удалить элементы с id " + ",".join(ids),
        ("нет", "да"), 1, False)
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        valid = QMessageBox.question(
            self, '', "Действительно удалить элементы с id " + ",".join(ids),
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute("DELETE FROM films WHERE id IN (" + ", ".join(
                '?' * len(ids)) + ")", ids)
            self.con.commit()

    def save_results(self):
        if self.modified:
            cur = self.con.cursor()
            que = "UPDATE films SET\n"
            que += ", ".join([f"{key}='{self.modified.get(key)}'"
                              for key in self.modified.keys()])
            que += "WHERE id = ?"
            print(que)
            cur.execute(que, (self.spinBox.text(),))
            self.con.commit()
            self.modified.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
