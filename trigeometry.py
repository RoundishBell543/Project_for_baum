import sys
import numpy as np
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
)
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas
)
from matplotlib.figure import Figure


class TrigonometricPlotter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Графики тригонометрических функций")
        self.setGeometry(100, 100, 800, 600)

        # Основной виджет
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        # Основной Layout
        layout = QVBoxLayout(self.main_widget)

        # Поле ввода функции
        self.label = QLabel(
            "Введите функцию (например, np.sin(x), np.cos(x), np.tan(x), 1/np.tan(x)):",
            self,
        )
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
            x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
            # Вычисление значений y по введённой функции
            y = [eval(function_text, {"x": val, "np": np}) for val in x]

            # Построение графика
            ax.plot(x, y, label=f"y = {function_text}", color="blue")
            ax.set_title("График тригонометрической функции")
            ax.set_xlabel("x (радианы)")
            ax.set_ylabel("y")
            ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
            ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
            ax.legend()
            ax.grid()

            # Отобразить график
            self.canvas.draw()
        except Exception as e:
            # В случае ошибки показать сообщение
            ax.text(
                0.5,
                0.5,
                f"Ошибка: {e}",
                fontsize=12,
                ha="center",
                transform=ax.transAxes,
            )
            self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TrigonometricPlotter()
    window.show()
    sys.exit(app.exec())