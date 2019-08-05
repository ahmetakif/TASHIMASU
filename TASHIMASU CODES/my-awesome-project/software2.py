print " "
print "Welcome to software of the senior robot of Ahmet Akif KAYA the TASHIMASU"
print " "
print "This is for the raspberry pi of which the robot brings you some drinks"
print " "
print "Kocaeli, 2018"
print " "
print "ELEC_HARDWARE:"
print "A Raspberry Pi 3"
print "Two Arduino Uno's"
print "An Esp8266 NodeMCU"
print
print "Python 2.7.4"
print "OpenCV 3.1.0"
print
print "ATTENTION! Before running this software enter these to the terminal:"
print "source ~/.profile"
print "workon cv"
print " "
print "Enter the command 'help' for the meanings of keyboard control commands"
print " "

def helpcommands():
    print "|-----Meanings of keyboard control commands-----|"
    print "'w' = Goes forward"
    print "'s' = Goes backward"
    print "'a' = Pivot turns to the left"
    print "'d' = Pivot turns to the right"
    print "'q' = Turns to the left"
    print "'e' = Turns to the right"
    print "'1' = Fetches the first drink"
    print "'2' = Fetches the second drink"
    print "'3' = Fetches the mixed drink" 
    print "'4' = Stops all the pumps"
    print "'5' = Runs the first pump"
    print "'6' = Runs the second pump"
    print "'7' = Resverses the first pump to clean out"
    print "'8' = Resverses the second pump to clean out" 
    print "'9' = Resverses the both pumps to clean out"
    print "'u' = Measures distance to the closest object in front"
    print "'n' = Measures distance to the closest object in back"
    print "'h' = Measures distance to the closest object in left"
    print "'k' = Measures distance to the closest object in right"
    print "'p' = Turns the head 10 degrees up"
    print "'.' = Turns the head 10 degrees down"
    print "'l' = Turns the head 10 degrees left"
    print "'i' = Turns the head 10 degrees right"
    print "'-' = Centers the head vertically"
    print "'*' = Centers the head horizontally"
    print "'fan' = Showing the forward-sliding animation with randomized color"
    print "'ban' = Showing the backward-sliding animation with red color"
    print "'ran' = Showing the right-sliding animation with blue color"
    print "'lan' = Showing the left-sliding animation with blue color"
    print "'rpan' = Showing the whole spin right-sliding animation with green color"
    print "'lpan' = Showing the whole spin left-sliding animation with green color"
    print "'auto' = Enables the autonomous mode"
    print "'disco' = Enables disco styled ligthing"
    print "'face' = Detects wheter there is a face or not and tracks it's coordinates"
    print "'exit', 'quit', 'escape', 'suspense' = Quits the program"
    print " "

#IMPORTMENTS
import serial
#import sys
import time
#import json
import RPi.GPIO as gpio
from soundeffects import s1, s2
from face2 import detectface
import random

#ARDUINO SERIAL
a = serial.Serial('/dev/ttyACM0',9600)
b = serial.Serial('/dev/ttyACM1',9600)
#esp = serial.Serial('/dev/ttyUSB0',9600)

#VARIABLES
servoudangle = 90 #Default vertical servo angle
servolrangle = 90 #Default horizontal servo angle
usefulreturnthing = 0 #Variable for using for various return tasks
minimalfacesizetoserve = 100 #This value is meant to be in pixels

#gpio.setwarnings(False)
#gpio.setmode(gpio.BCM)
#gpio.setup(18,gpio.OUT)
#with open('word.json') as json_data:
#    d = json.load(json_data)
#if d == 0:
#    bringthedrink(0)
#    print "no"
#    gpio.output(18,0)
#elif d == 1:
#    bringthedrink(1)
#    print "yes"
#    gpio.output(18,1)
#elif d == 2:
#    bringthedrink(2)
#else:
#    print "Error: INVALID DRINK TYPE"#
#
#sys.stdout.flush()

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
def servou():
    a.write('K')
def servod():
    a.write('k')
def servol():
    a.write('L')
def servor():
    a.write('l')
def servoudmid():
    a.write('Z')
def servolrmid():
    a.write('z')
def stopfilling():
    a.write('m')
def cleanpump1():
    a.write('o')
def cleanpump2():
    a.write('p')
def cleanpump12():
    a.write('r')


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
def disco():
    b.write('D')
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
    faceval = searcharound()
    time.sleep(1)
    cometotheface(faceval)
    time.sleep(1)
    s1()
    if drinktype == 0:
        fillfrom1()
        time.sleep(20)
    elif drinktype == 1:
        fillfrom2()
        time.sleep(20)
    elif drinktype == 2:
        fillfrom12mix()
        time.sleep(25)
    else:
        print "Error: INVALID DRINK TYPE"
    stopfilling()
    s2()

def automode():
    fan()
    while True:
        serialData = int(esp.readline())
        if serialData == 0:
            bringthedrink(0)
        elif serialData == 1:
            bringthedrink(1)
        elif serialData == 2:
            bringthedrink(2)
        else:
            print "Error: INVALID DRINK TYPE"

def searcharound():
    global usefulreturnthing
    while True:
        faceval = detectface()
        if len(faceval) > 1:
            print "OH! HELLO THERE, FETCHING YOUR DRINK RIGHT NOW"
            return faceval
        else:
            usefulreturnthing = total180headsearch()
            if usefulreturnthing != 0:
                return usefulreturnthing
            else:
                changeverticalheadpose(50)
                usefulreturnthing = total180headsearch()
                if usefulreturnthing != 0:
                    return usefulreturnthing
                else:
                    changeverticalheadpose(90)
                    turnaround()
                    
def changeverticalheadpose(angle):
    global servoudangle
    for i in range(0, abs(angle - servoudangle)/10):
        if angle < servoudangle:
            servou()
        else:
            servod()
    servoudangle = angle    

def lookaround(xxval, yyval):
    global servolrangle
    global servoudangle
    for i in range(0, abs(xxval - servolrangle)/10):
        faceval = detectface()
        if len(faceval) > 1:
            print "OH! HELLO THERE, FETCHING YOUR DRINK RIGHT NOW"
            return faceval
        else:
            if xxval < servolrangle:
                servol()
            else:
                servor()
        time.sleep(0.1)
    servolrangle = xxval
    return 0

def turnaround():
    x = random.randint(0,2)
    if x == 0:
        mrightp(random.randint(1,6))
    else:
        mleftp(random.randint(1,6))

def total180headsearch():
    x = random.randint(0,2)
    global usefulreturnthing
    if x == 0:
        usefulreturnthing = lookaround(0,90)
        if usefulreturnthing != 0:
            return usefulreturnthing
        else:
            time.sleep(0.1)
            usefulreturnthing = lookaround(180,90)
            if usefulreturnthing != 0:
                return usefulreturnthing
            else:
                time.sleep(0.1)
                usefulreturnthing = lookaround(90,90)
                if usefulreturnthing != 0:
                    return usefulreturnthing
    else:
        usefulreturnthing = lookaround(180,90)
        if usefulreturnthing != 0:
            return usefulreturnthing
        else:
            time.sleep(0.1)
            usefulreturnthing = lookaround(0,90)
            if usefulreturnthing != 0:
                return usefulreturnthing
            else:
                time.sleep(0.1)
                usefulreturnthing = lookaround(90,90)
                if usefulreturnthing != 0:
                    return usefulreturnthing
    return 0

def cometotheface(faceval):
    global minimalfacesizetoserve
    turntotheface(faceval)
    time.sleep(1)
    if faceval[3] < minimalfacesizetoserve:
        mforward(float(abs(minimalfacesizetoserve-faceval[3]))/10.0)

def turntotheface(faceval):
    global servoudangle
    global servolrangle
    if servolrangle != 90:
        if servoudangle != 90:
            servoudmid()
        servolrmid()
        if servolrangle < 90:
            mrightp(float(abs(90-servolrangle))/10.0)
        else:
            mleftp(float(abs(90-servolrangle))/10.0)
        servolrangle = 90

#DEBUGGING AND CONTROLLING REMOTELY
while True:
    y = raw_input("Command: ")
    if y == "w":
        print "Going forward"
        mforward(1)
    elif y == "s":
        print "Going backward"
        mbackward(1)
    elif y == "a":
        print "Turning left"
        mleftp(1)
    elif y == "d":
        print "Turning right"
        mrightp(1)
    elif y == "q":
        print "Going to the left"
        mleft(1)
    elif y == "e":
        print "Going to the right"
        mright(1)
    elif y == "1":
        print "Fetching the first drink"
        bringthedrink(0)
    elif y == "2":
        print "Fetching the second drink"
        bringthedrink(1)
    elif y == "3":
        print "Fetching the mixed drink"
        bringthedrink(2)
    elif y == "4":
        print "Stopping all the pumps"
        stopfilling()
    elif y == "5":
        print "Running the first pump"
	fillfrom1()
    elif y == "6":
        print "Running the second pump"
        fillfrom2()
    elif y == "7":
        print "Reversing the first pump to clean out"
        cleanpump1()
    elif y == "8":
        print "Reversing the second pump to clean out"
        cleanpump2()
    elif y == "9":
        print "Resversing the both pumps to clean out"
        cleanpump12()
    elif y == "u":
        print "Measured distance to the closest object in front: "
        y = measuref()
        print y
    elif y == "n":
        print "Measured distance to the closest object in back: "
        y = measureb()
        print y
    elif y == "h":
        print "Measured distance to the closest object in left: "
        y = measurel()
        print y
    elif y == "k":
        print "Measured distance to the closest object in right: "
        y = measurer()
        print y
    elif y == "p":
        print "Head turning 10 degrees up"
        servoudangle = servoudangle - 10
        print servoudangle
        servou()
    elif y == ".":
        print "Head turning 10 degrees down" 
        servoudangle = servoudangle + 10
        print servoudangle
        servod()
    elif y == "l":
        print "Head turning 10 degrees left" 
        servolrangle = servolrangle - 10
        print servolrangle
        servol()
    elif y == "i":
        print "Head turning 10 degrees right" 
        servolrangle = servolrangle + 10
        print servolrangle
        servor()
    elif y == "-":
        print "Centering the head vertically"
        servoudangle = 90
        print servoudangle
        servoudmid()
    elif y == "*":
        print "Centering the head horizontally"
        servolrangle = 90
        print servolrangle
        servolrmid()
    elif y == "fan":
        print "Showing the forward-sliding animation with randomized color"
        fan()
    elif y == "ban":
        print "Showing the backward-sliding animation with red color"
        ban()
    elif y == "ran":
        print "Showing the right-sliding animation with blue color"
        ran()
    elif y == "lan":
        print "Showing the left-sliding animation with blue color"
        lan()
    elif y == "rpan":
        print "Showing the whole spin right-sliding animation with green color"
        rpan()
    elif y == "lpan":
        print "Showing the whole spin right-sliding animation with green color"
        lpan()
    elif y == "auto":
        print ">--AUTONOMOUS MODE IS ENABLED!--<"
        print "Now the TASHIMASU will wait for the commands from Google Assistant server and behave automatically"
        print "To exit please try control+c"
        automode()
    elif y == "disco":
        print "Disco style lighting is enabled"
        print "LETS PARTY DUDES"
        disco()
    elif y == "face":
        print "Looking for any faces around..."
        r = detectface()
        print r
    elif y == "exit" or y == "quit" or y == "escape" or y == "suspense":
        print "Quitting the main program, hope to see you soon -TASHIMASU"
        break
    elif y == "help":
        helpcommands()
    else:
        print "This command does not exist please try another or check the guide above"
        stopp()
