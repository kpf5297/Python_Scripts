import tkinter as tk
from tkinter import messagebox

def total_nodal_delay_calculator():
    def calculate_delay():
        try:
            # Retrieve user inputs
            packet_length = int(packet_length_entry.get())
            transmission_rate1 = int(transmission_rate1_entry.get())
            distance1 = float(distance1_entry.get())
            propagation_speed1 = float(propagation_speed1_entry.get())

            transmission_rate2 = int(transmission_rate2_entry.get())
            distance2 = float(distance2_entry.get())
            propagation_speed2 = float(propagation_speed2_entry.get())

            transmission_rate3 = int(transmission_rate3_entry.get())
            distance3 = float(distance3_entry.get())
            propagation_speed3 = float(propagation_speed3_entry.get())

            transmission_rate4 = int(transmission_rate4_entry.get())
            distance4 = float(distance4_entry.get())
            propagation_speed4 = float(propagation_speed4_entry.get())

            processing_delay1 = float(processing_delay1_entry.get())
            queuing_delay1 = float(queuing_delay1_entry.get())

            processing_delay2 = float(processing_delay2_entry.get())
            queuing_delay2 = float(queuing_delay2_entry.get())

            processing_delay3 = float(processing_delay3_entry.get())
            queuing_delay3 = float(queuing_delay3_entry.get())

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
            result_label.config(text=f'Total End-to-End Delay: {dend_end:.2f} seconds')
        except ValueError:
            # Display error message if inputs are invalid
            messagebox.showerror('Input Error', 'Please enter valid numbers for all fields')

    # Create the main window
    root = tk.Tk()
    root.title('Total Nodal Delay Calculator')
    root.geometry('500x700')

    # Create UI controls for user inputs
    tk.Label(root, text='Packet Length (bytes):').place(x=50, y=50)
    packet_length_entry = tk.Entry(root)
    packet_length_entry.place(x=300, y=50)

    tk.Label(root, text='Transmission Rate 1 (bps):').place(x=50, y=100)
    transmission_rate1_entry = tk.Entry(root)
    transmission_rate1_entry.place(x=300, y=100)

    tk.Label(root, text='Distance 1 (km):').place(x=50, y=150)
    distance1_entry = tk.Entry(root)
    distance1_entry.place(x=300, y=150)

    tk.Label(root, text='Propagation Speed 1 (m/s):').place(x=50, y=200)
    propagation_speed1_entry = tk.Entry(root)
    propagation_speed1_entry.place(x=300, y=200)

    tk.Label(root, text='Transmission Rate 2 (bps):').place(x=50, y=250)
    transmission_rate2_entry = tk.Entry(root)
    transmission_rate2_entry.place(x=300, y=250)

    tk.Label(root, text='Distance 2 (km):').place(x=50, y=300)
    distance2_entry = tk.Entry(root)
    distance2_entry.place(x=300, y=300)

    tk.Label(root, text='Propagation Speed 2 (m/s):').place(x=50, y=350)
    propagation_speed2_entry = tk.Entry(root)
    propagation_speed2_entry.place(x=300, y=350)

    tk.Label(root, text='Transmission Rate 3 (bps):').place(x=50, y=400)
    transmission_rate3_entry = tk.Entry(root)
    transmission_rate3_entry.place(x=300, y=400)

    tk.Label(root, text='Distance 3 (km):').place(x=50, y=450)
    distance3_entry = tk.Entry(root)
    distance3_entry.place(x=300, y=450)

    tk.Label(root, text='Propagation Speed 3 (m/s):').place(x=50, y=500)
    propagation_speed3_entry = tk.Entry(root)
    propagation_speed3_entry.place(x=300, y=500)

    tk.Label(root, text='Transmission Rate 4 (bps):').place(x=50, y=550)
    transmission_rate4_entry = tk.Entry(root)
    transmission_rate4_entry.place(x=300, y=550)

    tk.Label(root, text='Distance 4 (km):').place(x=50, y=600)
    distance4_entry = tk.Entry(root)
    distance4_entry.place(x=300, y=600)

    tk.Label(root, text='Propagation Speed 4 (m/s):').place(x=50, y=650)
    propagation_speed4_entry = tk.Entry(root)
    propagation_speed4_entry.place(x=300, y=650)

    tk.Label(root, text='Processing Delay 1 (sec):').place(x=50, y=700)
    processing_delay1_entry = tk.Entry(root)
    processing_delay1_entry.place(x=300, y=700)

    tk.Label(root, text='Queuing Delay 1 (sec):').place(x=50, y=750)
    queuing_delay1_entry = tk.Entry(root)
    queuing_delay1_entry.place(x=300, y=750)

    tk.Label(root, text='Processing Delay 2 (sec):').place(x=50, y=800)
    processing_delay2_entry = tk.Entry(root)
    processing_delay2_entry.place(x=300, y=800)

    tk.Label(root, text='Queuing Delay 2 (sec):').place(x=50, y=850)
    queuing_delay2_entry = tk.Entry(root)
    queuing_delay2_entry.place(x=300, y=850)

    tk.Label(root, text='Processing Delay 3 (sec):').place(x=50, y=900)
    processing_delay3_entry = tk.Entry(root)
    processing_delay3_entry.place(x=300, y=900)

    tk.Label(root, text='Queuing Delay 3 (sec):').place(x=50, y=950)
    queuing_delay3_entry = tk.Entry(root)
    queuing_delay3_entry.place(x=300, y=950)

    # Create a button to calculate the total nodal delay
    calculate_button = tk.Button(root, text='Calculate', command=calculate_delay)
    calculate_button.place(x=200, y=1000)

    # Create a label for displaying the result
    result_label = tk.Label(root, text='Total End-to-End Delay: N/A')
    result_label.place(x=50, y=1050)

    # Run the main event loop
    root.mainloop()

total_nodal_delay_calculator()
