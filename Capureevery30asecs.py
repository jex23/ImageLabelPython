import cv2
from PIL import Image, ImageTk
import tkinter as tk
import os
import time

def update_frame():
    global running
    ret, frame = cap.read()

    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=img)

        # Update the image on the panel
        panel.img = img
        panel.config(image=img)

    if running:
        update_elapsed_time()

    # Call update_frame function after 10 milliseconds
    root.after(10, update_frame)

def update_elapsed_time():
    # Implement your logic for updating elapsed time here
    pass

def capture_frame_periodic():
    if running:
        ret, frame = cap.read()
        if ret:
            folder_name = time.strftime("%B-%d-%Y", time.localtime())  # Month-Date-Year format

            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            time_label = time.strftime("%I_%M_%S_%p", time.localtime())
            img_name = os.path.join(folder_name, f'{time_label}.jpg')
            cv2.imwrite(img_name, frame)
            print(f"Frame captured and saved: {img_name}")

        # Schedule the function to be called again after 30 seconds
        root.after(30000, capture_frame_periodic)

def toggle_capture():
    global running
    if running:
        capture_button.config(text="Capture every 30 seconds Off")
        running = False
    else:
        capture_button.config(text="Capture every 30 seconds On")
        running = True
        # Call the function to start periodic capture
        capture_frame_periodic()

# Create the main Tkinter window
root = tk.Tk()
root.title("Webcam Viewer")

# Open the webcam using OpenCV
cap = cv2.VideoCapture(0)  # 0 represents the default webcam, you can change it if you have multiple cameras

# Set the dimensions of the window
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Create a panel to display the video frames
panel = tk.Label(root)
panel.pack(padx=10, pady=10)

# Create a capture button
capture_button = tk.Button(root, text="Capture every 30 seconds Off", command=toggle_capture)
capture_button.pack(pady=10)

# Initialize the running variable
running = False

# Start updating the frame
update_frame()

# Run the Tkinter event loop
root.mainloop()

# Release the video capture object
cap.release()
