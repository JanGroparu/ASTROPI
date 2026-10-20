from PIL import Image
import matplotlib.pyplot as plt

from sense_hat import SenseHat
from picamzero import Camera
from time import sleep

def getTime(angularSpeed):
    Pixelv = 3040 # pixels
    mpp = 130 # meters
    Rezv = Pixelv * mpp 
    earthRadius = 6371008.8 # meters
    t = Rezv / (angularSpeed * earthRadius)
    return t 

sense_hat = SenseHat()
camera = Camera()

camera.take_photo("image1.jpg")
timeToSleep = getTime(0.001128)
sleep(10)
camera.take_photo("image2.jpg")
sleep(10)
camera.take_photo("image3.jpg")
sleep(10)
camera.take_photo("image4.jpg")
sleep(10)
camera.take_photo("image5.jpg")
sleep(10)
camera.take_photo("image6.jpg")
print()

img1 = Image.open("image1.jpg")
img2 = Image.open("image2.jpg")

img3 = Image.new("RGB", (4056, 6080), "white")

img3.paste(img1, (0, 0))
img3.paste(img2, (0, 3040))

img3.save("output.jpg")