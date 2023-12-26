"""Calculates the average speed depending on the metrics given"""
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox


class AverageSpeedCalculator(QWidget):
    """This is the GUI design of the Average Speed Calculator"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create Widgets

        distance_label = QLabel("Distance: ")
        self.distance_line_edit = QLineEdit()

        self.combo = QComboBox()
        self.combo.addItems(['Metric(km)', 'Imperial(miles)'])

        time_label = QLabel("Time (hours): ")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)

        self.result_label = QLabel("Result")

        # Add Widget to Grid

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.result_label, 3, 0, 1, 2)

        # Allow grid labels to be shown
        self.setLayout(grid)

    def calculate_speed(self):
        """Calculate the Speed"""
        # Get distance and time from the input boxes
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())

        # Calculate average speed
        speed = distance/time

       # Check what user chose in the combo
        if self.combo.currentText() == 'Metric(km)':
            speed = round(speed, 2)
            unit = 'km/h'

        if self.combo.currentText() == 'Imperial(miles)':
            speed = round(speed * 0.621371, 2)
            unit = 'mph'

        # Display the result
        self.result_label.setText(f"Average Speed: {speed} {unit}")


app = QApplication(sys.argv)
avg_speed_calculator = AverageSpeedCalculator()
avg_speed_calculator.show()
sys.exit(app.exec())
