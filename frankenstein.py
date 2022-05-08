#!/usr/bin/python
import RPi.GPIO as GPIO
import time

digitOne = 16
digitTwo = 37

aPin = 11
bPin = 22
cPin = 15
dPin = 29
ePin = 31
fPin = 33
gPin = 36

buttonOne = 13
buttonTwo = 18

ledPin = 32

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(buttonOne, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonTwo, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(digitOne, GPIO.OUT)
GPIO.setup(digitTwo, GPIO.OUT)

GPIO.setup(aPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)
GPIO.setup(cPin, GPIO.OUT)
GPIO.setup(dPin, GPIO.OUT)
GPIO.setup(ePin, GPIO.OUT)
GPIO.setup(fPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)

def digitOneOn():
    GPIO.output(digitOne, GPIO.HIGH)
    GPIO.output(digitTwo, GPIO.LOW)

def digitTwoOn():
    GPIO.output(digitOne, GPIO.LOW)
    GPIO.output(digitTwo, GPIO.HIGH)


def displayOff():
    GPIO.output(digitOne, GPIO.LOW)

    GPIO.output(aPin, GPIO.HIGH)
    GPIO.output(bPin, GPIO.HIGH)
    GPIO.output(cPin, GPIO.HIGH)
    GPIO.output(dPin, GPIO.HIGH)
    GPIO.output(ePin, GPIO.HIGH)
    GPIO.output(fPin, GPIO.HIGH)
    GPIO.output(gPin, GPIO.HIGH)

def displayOne():
    GPIO.output(bPin, GPIO.LOW)
    GPIO.output(cPin, GPIO.LOW)

    GPIO.output(aPin, GPIO.HIGH)
    GPIO.output(dPin, GPIO.HIGH)
    GPIO.output(ePin, GPIO.HIGH)
    GPIO.output(fPin, GPIO.HIGH)
    GPIO.output(gPin, GPIO.HIGH)

def displayTwo():
    GPIO.output(aPin, GPIO.LOW)
    GPIO.output(bPin, GPIO.LOW)
    GPIO.output(dPin, GPIO.LOW)
    GPIO.output(ePin, GPIO.LOW)
    GPIO.output(gPin, GPIO.LOW)

    GPIO.output(cPin, GPIO.HIGH)
    GPIO.output(fPin, GPIO.HIGH)

def displayThree():
    GPIO.output(aPin, GPIO.LOW)
    GPIO.output(bPin, GPIO.LOW)
    GPIO.output(cPin, GPIO.LOW)
    GPIO.output(dPin, GPIO.LOW)
    GPIO.output(gPin, GPIO.LOW)

    GPIO.output(ePin, GPIO.HIGH)
    GPIO.output(fPin, GPIO.HIGH)

def displayFour():
    GPIO.output(bPin, GPIO.LOW)
    GPIO.output(cPin, GPIO.LOW)
    GPIO.output(fPin, GPIO.LOW)
    GPIO.output(gPin, GPIO.LOW)

    GPIO.output(aPin, GPIO.HIGH)
    GPIO.output(dPin, GPIO.HIGH)
    GPIO.output(ePin, GPIO.HIGH)


def displayFive():
    GPIO.output(aPin, GPIO.LOW)
    GPIO.output(cPin, GPIO.LOW)
    GPIO.output(dPin, GPIO.LOW)
    GPIO.output(fPin, GPIO.LOW)
    GPIO.output(gPin, GPIO.LOW)

    GPIO.output(bPin, GPIO.HIGH)
    GPIO.output(ePin, GPIO.HIGH)

def displaySix():
    GPIO.output(aPin, GPIO.LOW)
    GPIO.output(cPin, GPIO.LOW)
    GPIO.output(dPin, GPIO.LOW)
    GPIO.output(ePin, GPIO.LOW)
    GPIO.output(fPin, GPIO.LOW)
    GPIO.output(gPin, GPIO.LOW)

    GPIO.output(bPin, GPIO.HIGH)

def displaySeven():
    GPIO.output(aPin, GPIO.LOW)
    GPIO.output(bPin, GPIO.LOW)
    GPIO.output(cPin, GPIO.LOW)

    GPIO.output(dPin, GPIO.HIGH)
    GPIO.output(ePin, GPIO.HIGH)
    GPIO.output(fPin, GPIO.HIGH)
    GPIO.output(gPin, GPIO.HIGH)

def displayEight():
    GPIO.output(aPin, GPIO.LOW)
    GPIO.output(bPin, GPIO.LOW)
    GPIO.output(cPin, GPIO.LOW)
    GPIO.output(dPin, GPIO.LOW)
    GPIO.output(ePin, GPIO.LOW)
    GPIO.output(fPin, GPIO.LOW)
    GPIO.output(gPin, GPIO.LOW)

def displayNine():
    GPIO.output(aPin, GPIO.LOW)
    GPIO.output(bPin, GPIO.LOW)
    GPIO.output(cPin, GPIO.LOW)
    GPIO.output(gPin, GPIO.LOW)
    GPIO.output(fPin, GPIO.LOW)

    GPIO.output(dPin, GPIO.HIGH)
    GPIO.output(ePin, GPIO.HIGH)

def displayZero():
    GPIO.output(aPin, GPIO.LOW)
    GPIO.output(bPin, GPIO.LOW)
    GPIO.output(cPin, GPIO.LOW)
    GPIO.output(dPin, GPIO.LOW)
    GPIO.output(ePin, GPIO.LOW)
    GPIO.output(fPin, GPIO.LOW)

    GPIO.output(gPin, GPIO.HIGH)

digitOneOn()
displayNum = 0

while True:
    buttonOneState = GPIO.input(buttonOne)
    buttonTwoState = GPIO.input(buttonTwo)

    if buttonOneState == False: # if the button is pressed down
        if displayNum < 9:
            displayNum = displayNum + 1
        time.sleep(.5)

    if buttonTwoState == False: # if button two is pressed down
        if displayNum != 0:
            displayNum = displayNum - 1
        time.sleep(.5)

    if displayNum >= 5:
        GPIO.output(ledPin, GPIO.HIGH)

    if displayNum < 5:
        GPIO.output(ledPin, GPIO.LOW)

    if displayNum == 0:
        displayZero()

    if displayNum == 1:
        displayOne()

    if displayNum == 2:
        displayTwo()

    if displayNum == 3:
        displayThree()

    if displayNum == 4:
        displayFour()

    if displayNum == 5:
        displayFive()

    if displayNum == 6:
        displaySix()

    if displayNum == 7:
        displaySeven()

    if displayNum == 8:
        displayEight()

    if displayNum == 9:
        displayNine()



