import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
import main_window as mw
import line_widget as lw

class MainWindow(QMainWindow, mw.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def initUi(self):
        self.pushButton.clicked.connect(self.line_chart)
        self.pushButton_2.clicked.connect(self.trigonometric_function)

    def line_chart(self):
        self.window_line = Line_chart(self)
        self.window_line.show()
    def trigonometric_function(self):
        pass

    def three_D_chart(self):
        pass

class Line_chart(QWidget, lw.Ui_widget_1):
    def __init__(self):
        super().__init__()
        self.initUi(self)

    def initUi(self, *args):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())