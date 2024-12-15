import sqlite3
import sys
import random
import sqlite3 as sq
from PyQt6.QtGui import QPixmap
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget
from PyQt6.QtWidgets import QWidget, QLabel, QMessageBox, QCheckBox
from PyQt6.QtWidgets import QApplication, QTableView
import Project

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

useles_items = []

file_lows = open("Laws_text.txt", encoding='utf-8').read()
db = sqlite3.connect("base.db")
cur = db.cursor()
code_strings = {1: "Це мэхихт л щйъфо.",
                2: "Шчй бтьйхй фчтмэ.",
                3: "Ут нзхер те знчехй.",
                4: "Утн зучужнрн шлнт.",
                5: "Фг чцмэзур хз фцшм.",
                6: "Цхз тычруз хцйцм чузъдм.",
                7: "Яю бщвятрь ырбгщюд.",
                8: "Яющ ахьщ ахвюо.",
                9: "Оэ уорфтжнк цкнюо.",
                10: "Рпв скувнв скуюор."
                }

hint_to_code = {1: "Сдвиг на больший корень ур-ния х^2+3x-130.",
                2: "Сдвиг на больший корень ур-ния х^2+3x-130.",
                3: "Сдвиг на х, который удовлетворяет равенству 2^х = 32.",
                4: "Сдвиг на х, который удовлетворяет равенству 2^х = 32.",
                5: "Сдвиг на х, который является знаенателем дроби 0,625.",
                6: "Сдвиг на х, который является знаенателем дроби 0,625.",
                7: "Сдвиг на х, который удовлетворяет равенству ∛4913 = х.",
                8: "Сдвиг на х, который удовлетворяет равенству ∛4913 = х.",
                9: "Просто сдвиг на 2",
                10: "Просто сдвиг на 2"
                }
answer_to_code = {1: "Мы гуляли в парке.",
                  2: "Она читала книгу.",
                  3: "Он играл на гитаре.",
                  4: "Они готовили ужин.",
                  5: "Мы поехали на море.",
                  6: "Она купила новое платье.",
                  7: "Он рисовал картину.",
                  8: "Они пели песню.",
                  9: "Мы смотрели фильм.",
                  10: "Она писала письмо."
                  }


class MyWidget(QMainWindow, Project.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_code)
        self.pushButton_2.clicked.connect(self.checking_the_code)
        self.pushButton_3.clicked.connect(self.insert_to_base_winners)
        self.pushButton_4.clicked.connect(self.laws)
        self.pushButton_5.clicked.connect(self.watch_table_winners)
        self.pushButton_6.clicked.connect(self.get_hint)
        self.count = 0
        self.count_check = 0

    def get_code(self):
        self.n = random.choice(items)
        self.lineEdit.setText(code_strings[self.n])
        self.count_check += 1

    def closeEvent(self, event):
        valid = QMessageBox.question(
            self, 'Закрытие игры', "Вы дествительно хотите закончить игру?",
            buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if valid == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def checking_the_code(self):
        if self.lineEdit_2.text() == answer_to_code[self.n] and self.n not in useles_items:
            self.lineEdit_3.setText("Молодец, +1 очко")
            self.count += 1
            self.lcdNumber.display(self.count)
            useles_items.append(self.n)
        elif self.lineEdit_2.text() == answer_to_code[self.n] and self.n in useles_items:
            self.lineEdit_3.setText("Молодец, но этот шифр уже был)))")
        else:
            self.lineEdit_3.setText("Увы, неверно. Попробуй ещё раз.")

    def laws(self):
        self.window = Laws(self)
        self.window.show()

    def get_hint(self):
        self.windowl = Hints(self, self.n)
        self.windowl.show()

    def watch_table_winners(self):
        self.table = Winners_table(self)
        self.table.show()

    def insert_to_base_winners(self):
        self.id = 0
        self.id += 1
        self.nick_name = f"user number {self.id}"
        self.score = self.count
        cur.execute('''
            INSERT INTO winners (nick_name, score) VALUES(?, ?)
            ''', (self.nick_name, self.score))
        db.commit()



class Laws(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 900, 350)
        self.setWindowTitle("Правила игры")
        self.Lows_text = QLabel(self)
        self.Lows_text.setText(file_lows)
        self.pixmap = QPixmap('picture.png')
        self.image = QLabel(self)
        self.image.move(0, 80)
        self.image.resize(500, 300)
        self.image.setPixmap(self.pixmap)


class Hints(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.n = args[-1]
        self.initUI(args[:-1])

    def initUI(self, args):
        self.setGeometry(300, 300, 400, 50)
        self.setWindowTitle(f"Подсказка №{self.n}")
        self.hints = QLabel(self)
        self.hints.move(0, 0)
        self.hints.setText(hint_to_code[self.n])


class Winners_table(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("Таблица лучших игроков")

        d = QSqlDatabase.addDatabase('QSQLITE')
        d.setDatabaseName('base.db')
        d.open()
        view = QTableView(self)
        model = QSqlTableModel(self, d)
        model.setTable('winners')
        model.select()

        view.setModel(model)
        view.move(10,10)
        view.resize(500,500)
        self.setWindowTitle("")




def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
