from PIL import Image

path = str(input('Enter path of image'))
width = int(input("Enter width"))
height = int(input("Enter Height"))


with Image.open (Path) as im:
    resized = im.resize((width,height))
    resized.show()
