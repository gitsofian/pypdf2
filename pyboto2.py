from PIL import Image
from tkinter import filedialog
from tkinter.filedialog import askopenfile

# create new image by import
img = Image.open("./images/textract-resized.jpg")
# show the picture
img.show()


# alternative way to import image
with Image.open("./images/textract.jpg", mode="r", formats=None) as image:
    image.show()
 


def upload_file():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfile(mode="r", filetypes=f_types)
    if filename is not None:
        img = Image.open(filename, mode="r", formats=None)
        img.show()


# create a new image from scratch
# upload_file()
