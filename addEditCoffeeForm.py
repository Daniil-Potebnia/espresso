import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class Uploading(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButton.clicked.connect(self.ready)
        self.con = sqlite3.connect('coffee.sqlite')

    def ready(self):
        if (not self.lineEdit.text() or not self.lineEdit_2.text() or not self.lineEdit_3.text() or
                not self.lineEdit_4.text() or not self.lineEdit_3.text() or not self.lineEdit_6.text() or
                (self.lineEdit_3.text() != 'True' and self.lineEdit_3.text() != 'False') or
                not self.lineEdit_5.text().isdigit() or not self.lineEdit_6.text().isdigit()):
            self.label_7.setText('Неправильный формат ввода')
        else:
            cur = self.con.cursor()
            id_ = len(cur.execute(f'''SELECT * FROM coffee''').fetchall()) + 1
            bean = True if self.lineEdit_3.text() == 'True' else False
            cur.execute(f'''INSERT INTO coffee(id, name, roasting, bean, taste, price, amount) 
            VALUES({id_}, "{self.lineEdit.text()}", "{self.lineEdit_2.text()}", "{bean}", "{self.lineEdit_4.text()}", 
            {int(self.lineEdit_5.text())}, {int(self.lineEdit_6.text())})''')
            self.con.commit()
            self.close()
