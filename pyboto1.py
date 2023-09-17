import boto3
import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk


def upload_file():
    global img
    aws_mag_con = boto3.Session(profile_name="demo_user")
    boto3.client = aws_mag_con.client(service_name="textract", region_name="eu-central-2")
    
    f_types = [('Jpg Files', '*.jpg')]
    # filename = filedialog.askopenfile(mode="r", filetypes=f_types)
    with Image.open("./images/textract.jpg", mode="r", formats=None) as img:
        # img = Image.open(filename, mode="r", formats=None)
        # resizing the uploaded image
        # img.show()
        img_resized = img.resize((400, 200))
        img = ImageTk.PhotoImage(img_resized)

        b2 = tk.Button(my_w, image=img)
        b2.pack()


my_w = tk.Tk()
my_w.geometry("450x400")
my_w.title("AWS Textract")
my_font1 = ('times', 18, 'bold')
l1 = tk.Label(my_w, text="Upload an image",
              width=30, font=my_font1)
l1.pack()

# print(p.pilinfo(out=None, supported_formats=True))

b1 = tk.Button(my_w, text='Upload a file und see what it has!',
               width=30, command=lambda: upload_file())
b1.pack()

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)


my_w.mainloop()


