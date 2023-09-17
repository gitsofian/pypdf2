import boto3
from PIL import Image

filename = "./images/textract-resized.jpg"


def get_image_as_bytes(filename):
    with open(file=filename, mode="rb") as img_as_byte:
        return img_as_byte.read()


with Image.open(filename, mode="r", formats=None) as image:
    image.show()

img_as_bytes = get_image_as_bytes(filename)


s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

client = boto3.client("textract")
resp = client.detect_document_text(
    Document={
        "Bytes": img_as_bytes,
    }
)

for block in resp["Blocks"]:
    if block["BlockType"]=="LINE": #WORD or LINE
        print(block["Text"])