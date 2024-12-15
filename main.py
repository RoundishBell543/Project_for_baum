import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
import main_window as mw

class MainWindow(QMainWindow, mw.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.line_chart)
        self.pushButton_2.clicked.connect(self.trigonometric_function)

    def line_chart(self):
        pass
    def trigonometric_function(self):
        pass

    def three_D_chart(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())