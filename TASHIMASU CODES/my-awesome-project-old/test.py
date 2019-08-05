import RPi.GPIO as gpio

def init():
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    gpio.setup(18,gpio.OUT)

def led_on():
    init()
    gpio.output(18,1)

def led_off():
    init()
    gpio.output(18,0)
