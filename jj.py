import sys
import numpy as np
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PieChartApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Круговая диаграмма")
        self.setGeometry(100, 100, 800, 600)

        # Основной виджет
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        # Основной Layout
        layout = QVBoxLayout(self.main_widget)

        # Поле ввода данных
        self.label = QLabel(
            "Введите значения для круговой диаграммы, разделённые запятыми (например, 30, 40, 30):",
            self,
        )
        layout.addWidget(self.label)

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        # Кнопка построения
        self.plot_button = QPushButton("Построить диаграмму", self)
        self.plot_button.clicked.connect(self.plot_pie_chart)
        layout.addWidget(self.plot_button)

        # Полотно для графика
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

    def plot_pie_chart(self):
        # Получение данных от пользователя
        input_text = self.input_field.text()

        # Очистка предыдущего графика
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        try:
            # Преобразование введенных данных в список чисел
            data = list(map(float, input_text.split(",")))

            # Построение круговой диаграммы
            ax.pie(data, labels=[f"Сегмент {i+1}" for i in range(len(data))], autopct='%1.1f%%', startangle=90)
            ax.set_title("Круговая диаграмма")

            # Отобразить диаграмму
            self.canvas.draw()
        except ValueError:
            # В случае ошибки показать сообщение
            ax.text(0.5, 0.5, "Ошибка ввода", fontsize=12, ha='center', transform=ax.transAxes)
            self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PieChartApp()
    window.show()
    sys.exit(app.exec())