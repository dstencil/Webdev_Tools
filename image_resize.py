from PIL import Image

filepath = str(input('Enter path of image to resize: '))
savepath = str(input('Enter path to save image: '))
width = int(input("Enter width: "))
height = int(input("Enter Height: "))


with Image.open (filepath) as im:
    resized = im.resize((width,height))
    resized.save(savepath)
