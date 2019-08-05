#IMPORTMENTS
import serial
import time
import json
import RPi.GPIO as gpio
from soundeffects import s1, s2

#ARDUINO SERIAL
a = serial.Serial('/dev/ttyACM0',9600)
b = serial.Serial('/dev/ttyACM1',9600)

#VARIABLES
servoudangle = 90
servolrangle = 90

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)
with open('word.json') as json_data:
    d = json.load(json_data)
if d == 0:
    bringthedrink(0)
    gpio.output(18,1)
    time.sleep(0.1)
    gpio.output(18,0)
elif d == 1:
    bringthedrink(1)
    gpio.output(18,1)
    time.sleep(1)
    gpio.output(18,0)
elif d == 2:
    bringthedrink(2)
else:
    print "Error: INVALID DRINK TYPE"


#ARDUINO A
def forward():
    a.write('d')
def backward():
    a.write('c')
def left():
    a.write('e')
def right():
    a.write('f')
def leftp():
    a.write('a')
def rightp():
    a.write('b')
def stopp():
    a.write('g')
def fillfrom1():
    a.write('h')
def fillfrom2():
    a.write('i')
def fillfrom12mix():
    a.write('j')
def servoud(angle):
    a.write('k')
    time.sleep(0.05)
    a.write(angle)
def servolr(angle):
    a.write('l')
    time.sleep(0.05)
    a.write(angle)
def stopfilling():
    a.write('m')

#ARDUINO B
def measuref():
    b.write('a')
    time.sleep(0.005)
    distf = int(b.readline())
    return distf
def measureb():
    b.write('b')
    time.sleep(0.005)
    distb = int(b.readline())
    return distb
def measurel():
    b.write('c')
    time.sleep(0.005)
    distl = int(b.readline())
    return distl
def measurer():
    b.write('d')
    time.sleep(0.005)
    distr = int(b.readline())
    return distr
def fan():
    b.write('e')
    time.sleep(1)
def ban():
    b.write('f')
    time.sleep(1)
def lan():
    b.write('g')
    time.sleep(1)
def ran():
    b.write('h')
    time.sleep(1)
def lpan():
    b.write('i')
    time.sleep(1)
def rpan():
    b.write('j')
    time.sleep(1)

#MOVE FUNCTIONS
def mforward(tf):
    x = 0
    distf = measuref()
    distb = measureb()
    distl = measurel()
    distr = measurer()
    fan()
    while distf > 20 and distb > 20 and distl > 20 and distr > 20 and x < 100:
        distf = measuref()
        distb = measureb()
        distl = measurel()
        distr = measurer()
        x = x + 1
        forward()
        tf = float(tf)
        time.sleep(tf/100)
    stopp()
def mbackward(tf):
    x = 0
    distf = measuref()
    distb = measureb()
    distl = measurel()
    distr = measurer()
    ban()
    while distf > 20 and distb > 20 and distl > 20 and distr > 20 and x < 100:
        distf = measuref()
        distb = measureb()
        distl = measurel()
        distr = measurer()
        x = x + 1
        backward()
        tf = float(tf)
        time.sleep(tf/100)
    stopp()
def mleft(tf):
    x = 0
    distf = measuref()
    distb = measureb()
    distl = measurel()
    distr = measurer()
    lan()
    while distf > 20 and distb > 20 and distl > 20 and distr > 20 and x < 100:
        distf = measuref()
        distb = measureb()
        distl = measurel()
        distr = measurer()
        x = x + 1
        left()
        tf = float(tf)
        time.sleep(tf/100)
    stopp()
def mright(tf):
    x = 0
    distf = measuref()
    distb = measureb()
    distl = measurel()
    distr = measurer()
    ran()
    while distf > 20 and distb > 20 and distl > 20 and distr > 20 and x < 100:
        distf = measuref()
        distb = measureb()
        distl = measurel()
        distr = measurer()
        x = x + 1
        right()
        tf = float(tf)
        time.sleep(tf/100)
    stopp()
def mleftp(tf):
    x = 0
    distf = measuref()
    distb = measureb()
    distl = measurel()
    distr = measurer()
    lpan()
    while distf > 20 and distb > 20 and distl > 20 and distr > 20 and x < 100:
        distf = measuref()
        distb = measureb()
        distl = measurel()
        distr = measurer()
        x = x + 1
        leftp()
        tf = float(tf)
        time.sleep(tf/100)
    stopp()
def mrightp(tf):
    x = 0
    distf = measuref()
    distb = measureb()
    distl = measurel()
    distr = measurer()
    rpan()
    while distf > 20 and distb > 20 and distl > 20 and distr > 20 and x < 100:
        distf = measuref()
        distb = measureb()
        distl = measurel()
        distr = measurer()
        x = x + 1
        rightp()
        tf = float(tf)
        time.sleep(tf/100)
    stopp()

#MAIN TASK FUNCTIONS
def bringthedrink(drinktype):
    mforward(18)
    stopp()
    s1()
    if drinktype == 0:
        fillfrom1()
        time.sleep(10)
    elif drinktype == 1:
        fillfrom2()
        time.sleep(10)
    elif drinktype == 2:
        fillfrom12mix()
        time.sleep(5)
    else:
        print "Error: INVALID DRINK TYPE"
    stopfilling()
    s2()

"""/
#DEBUGGING
while True:
    y = raw_input("Komut: ")
    if y == "w":
        mforward(1)
    elif y == "s":
        mbackward(1)
    elif y == "a":
        mleftp(1)
    elif y == "d":
        mrightp(1)
    elif y == "q":
        mleft(1)
    elif y == "e":
        mright(1)
    elif y == "1":
        bringthedrink(0)
    elif y == "2":
        bringthedrink(1)
    elif y == "3":
        bringthedrink(2)
    elif y == "4":
        stopfilling()
    elif y == "5":
	fillfrom1()
    elif y == "u":
        y = measuref()
        print y
    elif y == "n":
        y = measureb()
        print y
    elif y == "h":
        y = measurel()
        print y
    elif y == "k":
        y = measurer()
        print y
    elif y == "p":
        servoudangle = servoudangle + 10
        servoud(servoudangle)
    elif y == ".":
        servoudangle = servoudangle - 10
        servoud(servoudangle)
    elif y == "l":
        servolrangle = servolrangle + 10
        servolr(servolrangle)
    elif y == ";":
        servoudangle = servoudangle - 10
        servolr(servolrangle)
    else:
        stopp()
"""
