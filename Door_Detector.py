'''
Created By:         James Rogers
Last Modified By:   James Rogers
Last Modified On:   01/06/2018
Purpose:            To detect if a door is open and send an email alert
'''

import RPi.GPIO as GPIO
import time

# Name the pins that we are using
GREEN = 14
YELLOW = 15
RED = 18
DOOR_OUT = 20
DOOR_IN = 21

# Disables the "This channel is already in use" warning
GPIO.setwarnings(False)

# Enable BCM numbering and set input/outputs
GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(DOOR_OUT, GPIO.OUT)
GPIO.setup(DOOR_IN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# DOOR_OUT should always be HIGH
GPIO.output(DOOR_OUT, GPIO.HIGH)

# DOOR_IN == 1 when door is closed
while True:
    if (GPIO.input(DOOR_IN) == 1):
        GPIO.output(GREEN, GPIO.HIGH)
        GPIO.output(YELLOW, GPIO.HIGH)
        GPIO.output(RED, GPIO.HIGH)

    else:
        GPIO.output(GREEN, GPIO.LOW)
        GPIO.output(YELLOW, GPIO.LOW)
        GPIO.output(RED, GPIO.LOW)

    time.sleep(1)

GPIO.cleanup()
