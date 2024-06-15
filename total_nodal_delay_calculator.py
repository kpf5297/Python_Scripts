import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox, QMessageBox

"""
Total Nodal Delay Calculator
Author: Kevin Fox
Date: June 15, 2024

Description:
This script creates a GUI application to calculate the total end-to-end nodal delay in a network.
The total nodal delay is calculated based on user inputs including packet length, transmission rates, distances,
propagation speeds, processing delays, and queuing delays for four different nodes. The formula used is:

Total Delay = sum of (Transmission Delay + Propagation Delay + Processing Delay + Queuing Delay) for all nodes

Transmission Delay (dtran) = Packet Length (L) / Transmission Rate
Propagation Delay (dprop) = Distance / Propagation Speed
"""

class NodalDelayCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Total Nodal Delay Calculator')
        self.setGeometry(100, 100, 600, 800)

        main_layout = QVBoxLayout()

        # Packet Length Group
        packet_length_group = QGroupBox("Packet Details")
        packet_length_layout = QGridLayout()
        packet_length_group.setLayout(packet_length_layout)
        self.packet_length_label = QLabel('Packet Length (bytes):')
        self.packet_length_input = QLineEdit('25')  # Default value: 200 bits / 8 bits per byte = 25 bytes
        packet_length_layout.addWidget(self.packet_length_label, 0, 0)
        packet_length_layout.addWidget(self.packet_length_input, 0, 1)
        main_layout.addWidget(packet_length_group)

        # Transmission and Propagation Group 1
        tp_group1 = QGroupBox("Transmission and Propagation 1")
        tp_layout1 = QGridLayout()
        tp_group1.setLayout(tp_layout1)
        self.transmission_rate1_label = QLabel('Transmission Rate 1 (bps):')
        self.transmission_rate1_input = QLineEdit('1000')  # Default value: 1 kbps
        self.distance1_label = QLabel('Distance 1 (km):')
        self.distance1_input = QLineEdit('10')  # Default value: 10 km
        self.propagation_speed1_label = QLabel('Propagation Speed 1 (m/s):')
        self.propagation_speed1_input = QLineEdit('1000000')  # Default value: 10x10^5 m/s = 1,000,000 m/s
        tp_layout1.addWidget(self.transmission_rate1_label, 0, 0)
        tp_layout1.addWidget(self.transmission_rate1_input, 0, 1)
        tp_layout1.addWidget(self.distance1_label, 1, 0)
        tp_layout1.addWidget(self.distance1_input, 1, 1)
        tp_layout1.addWidget(self.propagation_speed1_label, 2, 0)
        tp_layout1.addWidget(self.propagation_speed1_input, 2, 1)
        main_layout.addWidget(tp_group1)

        # Transmission and Propagation Group 2
        tp_group2 = QGroupBox("Transmission and Propagation 2")
        tp_layout2 = QGridLayout()
        tp_group2.setLayout(tp_layout2)
        self.transmission_rate2_label = QLabel('Transmission Rate 2 (bps):')
        self.transmission_rate2_input = QLineEdit('0')  # Default value: 0 for unused field
        self.distance2_label = QLabel('Distance 2 (km):')
        self.distance2_input = QLineEdit('0')  # Default value: 0 for unused field
        self.propagation_speed2_label = QLabel('Propagation Speed 2 (m/s):')
        self.propagation_speed2_input = QLineEdit('0')  # Default value: 0 for unused field
        tp_layout2.addWidget(self.transmission_rate2_label, 0, 0)
        tp_layout2.addWidget(self.transmission_rate2_input, 0, 1)
        tp_layout2.addWidget(self.distance2_label, 1, 0)
        tp_layout2.addWidget(self.distance2_input, 1, 1)
        tp_layout2.addWidget(self.propagation_speed2_label, 2, 0)
        tp_layout2.addWidget(self.propagation_speed2_input, 2, 1)
        main_layout.addWidget(tp_group2)

        # Transmission and Propagation Group 3
        tp_group3 = QGroupBox("Transmission and Propagation 3")
        tp_layout3 = QGridLayout()
        tp_group3.setLayout(tp_layout3)
        self.transmission_rate3_label = QLabel('Transmission Rate 3 (bps):')
        self.transmission_rate3_input = QLineEdit('0')  # Default value: 0 for unused field
        self.distance3_label = QLabel('Distance 3 (km):')
        self.distance3_input = QLineEdit('0')  # Default value: 0 for unused field
        self.propagation_speed3_label = QLabel('Propagation Speed 3 (m/s):')
        self.propagation_speed3_input = QLineEdit('0')  # Default value: 0 for unused field
        tp_layout3.addWidget(self.transmission_rate3_label, 0, 0)
        tp_layout3.addWidget(self.transmission_rate3_input, 0, 1)
        tp_layout3.addWidget(self.distance3_label, 1, 0)
        tp_layout3.addWidget(self.distance3_input, 1, 1)
        tp_layout3.addWidget(self.propagation_speed3_label, 2, 0)
        tp_layout3.addWidget(self.propagation_speed3_input, 2, 1)
        main_layout.addWidget(tp_group3)

        # Transmission and Propagation Group 4
        tp_group4 = QGroupBox("Transmission and Propagation 4")
        tp_layout4 = QGridLayout()
        tp_group4.setLayout(tp_layout4)
        self.transmission_rate4_label = QLabel('Transmission Rate 4 (bps):')
        self.transmission_rate4_input = QLineEdit('0')  # Default value: 0 for unused field
        self.distance4_label = QLabel('Distance 4 (km):')
        self.distance4_input = QLineEdit('0')  # Default value: 0 for unused field
        self.propagation_speed4_label = QLabel('Propagation Speed 4 (m/s):')
        self.propagation_speed4_input = QLineEdit('0')  # Default value: 0 for unused field
        tp_layout4.addWidget(self.transmission_rate4_label, 0, 0)
        tp_layout4.addWidget(self.transmission_rate4_input, 0, 1)
        tp_layout4.addWidget(self.distance4_label, 1, 0)
        tp_layout4.addWidget(self.distance4_input, 1, 1)
        tp_layout4.addWidget(self.propagation_speed4_label, 2, 0)
        tp_layout4.addWidget(self.propagation_speed4_input, 2, 1)
        main_layout.addWidget(tp_group4)

        # Delays Group
        delays_group = QGroupBox("Delays")
        delays_layout = QGridLayout()
        delays_group.setLayout(delays_layout)
        self.processing_delay1_label = QLabel('Processing Delay 1 (sec):')
        self.processing_delay1_input = QLineEdit('0')  # Default value: 0
        self.queuing_delay1_label = QLabel('Queuing Delay 1 (sec):')
        self.queuing_delay1_input = QLineEdit('0')  # Default value: 0
        self.processing_delay2_label = QLabel('Processing Delay 2 (sec):')
        self.processing_delay2_input = QLineEdit('0')  # Default value: 0 for unused field
        self.queuing_delay2_label = QLabel('Queuing Delay 2 (sec):')
        self.queuing_delay2_input = QLineEdit('0')  # Default value: 0 for unused field
        self.processing_delay3_label = QLabel('Processing Delay 3 (sec):')
        self.processing_delay3_input = QLineEdit('0')  # Default value: 0 for unused field
        self.queuing_delay3_label = QLabel('Queuing Delay 3 (sec):')
        self.queuing_delay3_input = QLineEdit('0')  # Default value: 0 for unused field
        delays_layout.addWidget(self.processing_delay1_label, 0, 0)
        delays_layout.addWidget(self.processing_delay1_input, 0, 1)
        delays_layout.addWidget(self.queuing_delay1_label, 1, 0)
        delays_layout.addWidget(self.queuing_delay1_input, 1, 1)
        delays_layout.addWidget(self.processing_delay2_label, 2, 0)
        delays_layout.addWidget(self.processing_delay2_input, 2, 1)
        delays_layout.addWidget(self.queuing_delay2_label, 3, 0)
        delays_layout.addWidget(self.queuing_delay2_input, 3, 1)
        delays_layout.addWidget(self.processing_delay3_label, 4, 0)
        delays_layout.addWidget(self.processing_delay3_input, 4, 1)
        delays_layout.addWidget(self.queuing_delay3_label, 5, 0)
        delays_layout.addWidget(self.queuing_delay3_input, 5, 1)
        main_layout.addWidget(delays_group)

        # Calculate button
        self.calculate_button = QPushButton('Calculate', self)
        self.calculate_button.clicked.connect(self.calculate_delay)
        main_layout.addWidget(self.calculate_button)

        # Result label
        self.result_label = QLabel('Total End-to-End Delay: N/A')
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

    def calculate_delay(self):
        try:
            # Retrieve and convert user inputs
            packet_length = int(self.packet_length_input.text())
            transmission_rate1 = int(self.transmission_rate1_input.text())
            distance1 = float(self.distance1_input.text())
            propagation_speed1 = float(self.propagation_speed1_input.text())

            transmission_rate2 = int(self.transmission_rate2_input.text())
            distance2 = float(self.distance2_input.text())
            propagation_speed2 = float(self.propagation_speed2_input.text())

            transmission_rate3 = int(self.transmission_rate3_input.text())
            distance3 = float(self.distance3_input.text())
            propagation_speed3 = float(self.propagation_speed3_input.text())

            transmission_rate4 = int(self.transmission_rate4_input.text())
            distance4 = float(self.distance4_input.text())
            propagation_speed4 = float(self.propagation_speed4_input.text())

            processing_delay1 = float(self.processing_delay1_input.text())
            queuing_delay1 = float(self.queuing_delay1_input.text())

            processing_delay2 = float(self.processing_delay2_input.text())
            queuing_delay2 = float(self.queuing_delay2_input.text())

            processing_delay3 = float(self.processing_delay3_input.text())
            queuing_delay3 = float(self.queuing_delay3_input.text())

            # Convert packet length to bits
            L = packet_length * 8

            # Initialize total end-to-end delay
            dend_end = 0

            # Calculate transmission and propagation delays for each node, if applicable
            if transmission_rate1 > 0 and propagation_speed1 > 0:
                dtran1 = L / transmission_rate1
                dprop1 = distance1 * 1000 / propagation_speed1
                dend_end += dtran1 + dprop1 + processing_delay1 + queuing_delay1

            if transmission_rate2 > 0 and propagation_speed2 > 0:
                dtran2 = L / transmission_rate2
                dprop2 = distance2 * 1000 / propagation_speed2
                dend_end += dtran2 + dprop2 + processing_delay2 + queuing_delay2

            if transmission_rate3 > 0 and propagation_speed3 > 0:
                dtran3 = L / transmission_rate3
                dprop3 = distance3 * 1000 / propagation_speed3
                dend_end += dtran3 + dprop3 + processing_delay3 + queuing_delay3

            if transmission_rate4 > 0 and propagation_speed4 > 0:
                dtran4 = L / transmission_rate4
                dprop4 = distance4 * 1000 / propagation_speed4
                dend_end += dtran4 + dprop4

            # Display the result
            self.result_label.setText(f'Total End-to-End Delay: {dend_end:.2f} seconds')
        except ValueError:
            # Display error message if inputs are invalid
            QMessageBox.critical(self, 'Input Error', 'Please enter valid numbers for all fields')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NodalDelayCalculator()
    ex.show()
    sys.exit(app.exec_())
