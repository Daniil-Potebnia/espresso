import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from addEditCoffeeForm import Uploading
from main_form import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.new_data)
        self.con = sqlite3.connect('data/coffee.sqlite')

    def new_data(self):
        self.new_form = Uploading()
        self.new_form.show()

    def start(self):
        cur = self.con.cursor()
        result = cur.execute(f'''SELECT * FROM coffee''').fetchall()
        if not result:
            return
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название сорта', 'Степень обжарки', 'Молотый/В зернах',
                                                    'Описание вкуса', 'Цена', 'Объем упаковки'])
        for i, row in enumerate(result):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
