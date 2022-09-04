import os

from PIL import Image, ImageTk
from urllib.request import urlopen
import tkinter

# app initials

app = tkinter.Tk()
app.title("Image Converter")
app.geometry("350x300")

# app icon
p1 = Image.open(urlopen("https://framalibre.org/sites/default/files/leslogos/application-icon.png"))
python_image = ImageTk.PhotoImage(p1)
app.iconphoto(False, python_image)


# functions

def convert():
    try:
        link = urlopen(URL_entry.get())
        im = Image.open(link).convert("RGB")
        image_path = "Converted Images"
        os.mkdir(image_path)
        im.save(f"{image_path}/" + output_entry.get())
    except:
        # result of error
        errorMessage = tkinter.StringVar()
        errorMessage_label = tkinter.Label(app, text="An Error \n Has occurred \n please close the \n app and retry",
                                           font=("bold", 11), foreground="Red")
        errorMessage_label.grid(row=4)


# Image Link
URL_text = tkinter.StringVar()
URL_label = tkinter.Label(app, text="Image Link: ", font=("bold", 13), pady=20)
URL_label.grid(row=0, column=0)
URL_entry = tkinter.Entry(app, textvariable=URL_text)
URL_entry.grid(row=0, column=1)

# Output Details
output_text = tkinter.StringVar()
output_label = tkinter.Label(app, text="filename.extension: ", font=("bold", 13), pady=20)
output_label.grid(row=1, column=0)

output_entry = tkinter.Entry(app, textvariable=output_text)
output_entry.grid(row=1, column=1)

# Button

downlaod_btn = tkinter.Button(app, text="Convert", width=12, command=convert)
downlaod_btn.grid(row=3, pady=20)

# Start program
app.mainloop()
