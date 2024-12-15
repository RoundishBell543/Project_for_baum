import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from sympy import sympify, lambdify

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Построение графиков")
        self.setGeometry(100, 100, 800, 600)

        # Основной виджет
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Вертикальный layout для основного виджета
        main_layout = QVBoxLayout(main_widget)

        # Поле для ввода функции
        self.function_input = QLineEdit(self)
        self.function_input.setPlaceholderText("Введите функцию (например, sin(x))")
        main_layout.addWidget(QLabel("Функция:"))
        main_layout.addWidget(self.function_input)

        # Поля для ввода диапазона
        range_layout = QHBoxLayout()
        self.start_input = QLineEdit(self)
        self.start_input.setPlaceholderText("Начало диапазона")
        self.end_input = QLineEdit(self)
        self.end_input.setPlaceholderText("Конец диапазона")
        range_layout.addWidget(QLabel("Диапазон:"))
        range_layout.addWidget(self.start_input)
        range_layout.addWidget(self.end_input)
        main_layout.addLayout(range_layout)

        # Кнопка для построения графика
        self.plot_button = QPushButton("Построить график", self)
        main_layout.addWidget(self.plot_button)

        # Кнопка для сохранения графика
        self.save_button = QPushButton("Сохранить график", self)
        main_layout.addWidget(self.save_button)

        # Создание области для графика
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        main_layout.addWidget(self.canvas)

        # Подключение кнопок к методам
        self.plot_button.clicked.connect(self.plot_function)
        self.save_button.clicked.connect(self.save_plot)

    def plot_function(self):
        # Получение введенных данных
        function_str = self.function_input.text()
        start = float(self.start_input.text())
        end = float(self.end_input.text())

        # Очистка предыдущего графика
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        # Создание массива значений x
        x = np.linspace(start, end, 400)

        # Использование Sympy для преобразования функции
        x_sym = sympify('x')
        function_sym = sympify(function_str)
        function_lambda = lambdify(x_sym, function_sym, 'numpy')

        # Построение графика
        ax.plot(x, function_lambda(x))
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title(f'График функции: {function_str}')
        ax.grid(True)

        # Обновление области графика
        self.canvas.draw()

    def save_plot(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить график", "",
                                                   "PNG (*.png);;JPEG (*.jpg *.jpeg);;All Files (*)")
        if file_name:
            self.figure.savefig(file_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())