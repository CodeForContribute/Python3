# import Image module
import functools
from PIL import Image

if __name__ == '__main__':
    # open the image
    catIm = Image.open('D:/1.jpg')

    # Display the dimensions of the image
    print(catIm.size)
