import sys
import numpy as np
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


class Plot3DApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D Графики")
        self.setGeometry(100, 100, 1000, 700)

        # Основной виджет
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        # Основной Layout
        layout = QVBoxLayout(self.main_widget)

        # Поле ввода функции
        self.label = QLabel(
            "Введите функцию от x и y (например, np.sin(np.sqrt(x**2 + y**2))):", self
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
        ax = self.figure.add_subplot(111, projection="3d")

        try:
            # Создание сетки значений x и y
            x = np.linspace(-5, 5, 100)
            y = np.linspace(-5, 5, 100)
            X, Y = np.meshgrid(x, y)

            # Вычисление значений z по введённой функции
            Z = eval(function_text, {"x": X, "y": Y, "np": np})

            # Построение 3D графика
            ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="k", alpha=0.8)
            ax.set_title("3D График функции")
            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            ax.set_zlabel("Z")

            # Отобразить график
            self.canvas.draw()
        except Exception as e:
            # В случае ошибки показать сообщение
            ax.text2D(
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
    window = Plot3DApp()
    window.show()
    sys.exit(app.exec())