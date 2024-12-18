import sys
import numpy as np
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
)
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas
)
from matplotlib.figure import Figure


class LinearFunctionPlotter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Построение линейной функции")
        self.setGeometry(100, 100, 800, 600)

        # Основной виджет
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        # Основной Layout
        layout = QVBoxLayout(self.main_widget)

        # Поле ввода функции
        self.label = QLabel("Введите линейную функцию (например, 2*x + 3):", self)
        layout.addWidget(self.label)

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        # Кнопка построения
        self.plot_button = QPushButton("Построить график", self)
        self.plot_button.clicked.connect(self.plot_graph)
        layout.addWidget(self.plot_button)

        # Полотно для графика
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

    def plot_graph(self):
        # Получение функции от пользователя
        function_text = self.input_field.text()

        # Очистка предыдущего графика
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        try:
            # Создание массива значений x
            x = np.linspace(-10, 10, 500)
            # Вычисление значений y по введённой функции
            y = [eval(function_text, {"x": val, "np": np}) for val in x]

            # Построение графика
            ax.plot(x, y, label=f"y = {function_text}", color='blue')
            ax.set_title("График линейной функции")
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.legend()
            ax.grid()

            # Отобразить график
            self.canvas.draw()
        except Exception as e:
            # В случае ошибки показать сообщение
            ax.text(0.5, 0.5, f"Ошибка: {e}", fontsize=12, ha='center', transform=ax.transAxes)
            self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LinearFunctionPlotter()
    window.show()
    sys.exit(app.exec())