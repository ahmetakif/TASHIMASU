import json
#from serialcomtest import bringthedrink
import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)

with open('word.json') as json_data:
    d = json.load(json_data)
if d == 0:
#    bringthedrink(0)
    gpio.output(18,1)
    time.sleep(1)
    gpio.output(18,0)
elif d == 1:
#    bringthedrink(1)
    gpio.output(18,1)
    time.sleep(200)
    gpio.output(18,0)
#elif d == 2:
#    bringthedrink(2)
#else:
#    print "Error: INVALID DRINK TYPE"




