import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class NodalDelayCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Total Nodal Delay Calculator')
        self.setGeometry(100, 100, 400, 600)

        layout = QVBoxLayout()

        # Packet Length
        self.packet_length_label = QLabel('Packet Length (bytes):')
        self.packet_length_input = QLineEdit()
        layout.addWidget(self.packet_length_label)
        layout.addWidget(self.packet_length_input)

        # Transmission Rate 1
        self.transmission_rate1_label = QLabel('Transmission Rate 1 (bps):')
        self.transmission_rate1_input = QLineEdit()
        layout.addWidget(self.transmission_rate1_label)
        layout.addWidget(self.transmission_rate1_input)

        # Distance 1
        self.distance1_label = QLabel('Distance 1 (km):')
        self.distance1_input = QLineEdit()
        layout.addWidget(self.distance1_label)
        layout.addWidget(self.distance1_input)

        # Propagation Speed 1
        self.propagation_speed1_label = QLabel('Propagation Speed 1 (m/s):')
        self.propagation_speed1_input = QLineEdit()
        layout.addWidget(self.propagation_speed1_label)
        layout.addWidget(self.propagation_speed1_input)

        # Transmission Rate 2
        self.transmission_rate2_label = QLabel('Transmission Rate 2 (bps):')
        self.transmission_rate2_input = QLineEdit()
        layout.addWidget(self.transmission_rate2_label)
        layout.addWidget(self.transmission_rate2_input)

        # Distance 2
        self.distance2_label = QLabel('Distance 2 (km):')
        self.distance2_input = QLineEdit()
        layout.addWidget(self.distance2_label)
        layout.addWidget(self.distance2_input)

        # Propagation Speed 2
        self.propagation_speed2_label = QLabel('Propagation Speed 2 (m/s):')
        self.propagation_speed2_input = QLineEdit()
        layout.addWidget(self.propagation_speed2_label)
        layout.addWidget(self.propagation_speed2_input)

        # Transmission Rate 3
        self.transmission_rate3_label = QLabel('Transmission Rate 3 (bps):')
        self.transmission_rate3_input = QLineEdit()
        layout.addWidget(self.transmission_rate3_label)
        layout.addWidget(self.transmission_rate3_input)

        # Distance 3
        self.distance3_label = QLabel('Distance 3 (km):')
        self.distance3_input = QLineEdit()
        layout.addWidget(self.distance3_label)
        layout.addWidget(self.distance3_input)

        # Propagation Speed 3
        self.propagation_speed3_label = QLabel('Propagation Speed 3 (m/s):')
        self.propagation_speed3_input = QLineEdit()
        layout.addWidget(self.propagation_speed3_label)
        layout.addWidget(self.propagation_speed3_input)

        # Transmission Rate 4
        self.transmission_rate4_label = QLabel('Transmission Rate 4 (bps):')
        self.transmission_rate4_input = QLineEdit()
        layout.addWidget(self.transmission_rate4_label)
        layout.addWidget(self.transmission_rate4_input)

        # Distance 4
        self.distance4_label = QLabel('Distance 4 (km):')
        self.distance4_input = QLineEdit()
        layout.addWidget(self.distance4_label)
        layout.addWidget(self.distance4_input)

        # Propagation Speed 4
        self.propagation_speed4_label = QLabel('Propagation Speed 4 (m/s):')
        self.propagation_speed4_input = QLineEdit()
        layout.addWidget(self.propagation_speed4_label)
        layout.addWidget(self.propagation_speed4_input)

        # Processing Delay 1
        self.processing_delay1_label = QLabel('Processing Delay 1 (sec):')
        self.processing_delay1_input = QLineEdit()
        layout.addWidget(self.processing_delay1_label)
        layout.addWidget(self.processing_delay1_input)

        # Queuing Delay 1
        self.queuing_delay1_label = QLabel('Queuing Delay 1 (sec):')
        self.queuing_delay1_input = QLineEdit()
        layout.addWidget(self.queuing_delay1_label)
        layout.addWidget(self.queuing_delay1_input)

        # Processing Delay 2
        self.processing_delay2_label = QLabel('Processing Delay 2 (sec):')
        self.processing_delay2_input = QLineEdit()
        layout.addWidget(self.processing_delay2_label)
        layout.addWidget(self.processing_delay2_input)

        # Queuing Delay 2
        self.queuing_delay2_label = QLabel('Queuing Delay 2 (sec):')
        self.queuing_delay2_input = QLineEdit()
        layout.addWidget(self.queuing_delay2_label)
        layout.addWidget(self.queuing_delay2_input)

        # Processing Delay 3
        self.processing_delay3_label = QLabel('Processing Delay 3 (sec):')
        self.processing_delay3_input = QLineEdit()
        layout.addWidget(self.processing_delay3_label)
        layout.addWidget(self.processing_delay3_input)

        # Queuing Delay 3
        self.queuing_delay3_label = QLabel('Queuing Delay 3 (sec):')
        self.queuing_delay3_input = QLineEdit()
        layout.addWidget(self.queuing_delay3_label)
        layout.addWidget(self.queuing_delay3_input)

        # Calculate button
        self.calculate_button = QPushButton('Calculate', self)
        self.calculate_button.clicked.connect(self.calculate_delay)
        layout.addWidget(self.calculate_button)

        # Result label
        self.result_label = QLabel('Total End-to-End Delay: N/A')
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_delay(self):
        try:
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

            # Calculate delays
            dtran1 = L / transmission_rate1
            dprop1 = distance1 * 1000 / propagation_speed1

            dtran2 = L / transmission_rate2
            dprop2 = distance2 * 1000 / propagation_speed2

            dtran3 = L / transmission_rate3
            dprop3 = distance3 * 1000 / propagation_speed3

            dtran4 = L / transmission_rate4
            dprop4 = distance4 * 1000 / propagation_speed4

            # Total end-to-end delay
            dend_end = (dtran1 + dprop1 + processing_delay1 + queuing_delay1 +
                        dtran2 + dprop2 + processing_delay2 + queuing_delay2 +
                        dtran3 + dprop3 + processing_delay3 + queuing_delay3 +
                        dtran4 + dprop4)

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
