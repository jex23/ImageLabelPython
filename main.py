import tkinter as tk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageDraw, ImageFont
import os

def add_text_to_images():
    input_folder = input_folder_path.get()
    output_folder = output_folder_path.get()
    text_to_write = text_entry.get()
    font_path = 'Font/Roboto-Black.ttf'  # Default font path
    font_size = font_size_scale.get()

    # Get selected color in hex and convert it to RGB
    selected_color_hex = color_hex.get()
    selected_color_rgb = tuple(int(selected_color_hex[i:i+2], 16) for i in (0, 2, 4))

    if not (os.path.isdir(input_folder) and os.path.isdir(output_folder) and os.path.isfile(font_path)):
        status_label.config(text="Invalid folders or font path!")
        return

    for filename in os.listdir(input_folder):
        if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            # Define the font for the text
            font = ImageFont.truetype(font_path, font_size)

            # Create a drawing context
            draw = ImageDraw.Draw(img)

            # Define the position where the text will be placed (top-left corner)
            text_position = (20, 20)  # Adjust the coordinates as needed

            # Draw the text on the image
            draw.text(text_position, text_to_write, fill=selected_color_rgb, font=font)

            # Save the image with the added text
            output_path = os.path.join(output_folder, f"modified_{filename}")
            img.save(output_path)

    status_label.config(text="Images with text added saved!")

def select_input_folder():
    folder_selected = filedialog.askdirectory()
    input_folder_path.set(folder_selected)

def select_output_folder():
    folder_selected = filedialog.askdirectory()
    output_folder_path.set(folder_selected)

def choose_text_color():
    color_code = colorchooser.askcolor(title="Choose Text Color")[1]
    color_hex.set(color_code[1:])  # Set color in hex format without the #

# Create the GUI window
root = tk.Tk()
root.title("Add Text to Images")

input_folder_path = tk.StringVar()
output_folder_path = tk.StringVar()
color_hex = tk.StringVar(value="000000")  # Default color: Black

# Input Folder
tk.Label(root, text="Select Input Folder:").pack()
input_frame = tk.Frame(root)
input_entry = tk.Entry(input_frame, textvariable=input_folder_path)
input_entry.pack(side=tk.LEFT)
input_button = tk.Button(input_frame, text="Browse", command=select_input_folder)
input_button.pack(side=tk.RIGHT)
input_frame.pack()

# Output Folder
tk.Label(root, text="Select Output Folder:").pack()
output_frame = tk.Frame(root)
output_entry = tk.Entry(output_frame, textvariable=output_folder_path)
output_entry.pack(side=tk.LEFT)
output_button = tk.Button(output_frame, text="Browse", command=select_output_folder)
output_button.pack(side=tk.RIGHT)
output_frame.pack()

# Text to Write
tk.Label(root, text="Enter Text to Write:").pack()
text_entry = tk.Entry(root)
text_entry.pack()

# Text Color
tk.Label(root, text="Select Text Color:").pack()
color_frame = tk.Frame(root)
color_entry = tk.Entry(color_frame, textvariable=color_hex)
color_entry.pack(side=tk.LEFT)
color_button = tk.Button(color_frame, text="Choose Color", command=choose_text_color)
color_button.pack(side=tk.RIGHT)
color_frame.pack()

# Font Size
tk.Label(root, text="Select Font Size:").pack()
font_size_scale = tk.Scale(root, from_=10, to=100, orient=tk.HORIZONTAL)
font_size_scale.set(30)  # Default font size
font_size_scale.pack()

# Add Text Button
add_text_button = tk.Button(root, text="Add Text to Images", command=add_text_to_images)
add_text_button.pack()

# Status Label
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
