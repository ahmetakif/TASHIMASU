from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(10)
camera.brightness = 50
camera.rotation = 180
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
