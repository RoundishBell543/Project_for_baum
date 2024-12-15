import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
import main_window as mw

class MainWindow(QMainWindow, mw.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.line_chart)
        self.pushButton_2.clicked.connect(self.trigonometric_function)

    def line_chart(self):
        self.window_line = Line_chart(self)
        self.window_line.show()
    def trigonometric_function(self):
        pass

    def three_D_chart(self):
        pass

class Line_chart(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUi(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Линейная функция")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())