import boto3
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk


def upload_file():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfile(filetypes=f_types)
    img = Image.open(filename)
    # resizing the uploaded image
    img_resize = img.resize((400, 200))
    img = ImageTk.PhotoImage(img_resize)

    b2 = tk.Button(my_w, Image=img)
    b2.pack()


my_w = tk.Tk()
my_w.geometry("450x400")
my_w.title("AWS Textract")
l1 = tk.Label(my_w, text="Upload an image",
              width=30, font=('times', 18, 'bold'))
b1 = tk.Button(my_w, text='Upload a file und see what it has!',
               width=30, command=upload_file)

b1.pack()

my_w.mainloop()


s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
