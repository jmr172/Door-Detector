'''
Created By:         James Rogers
Last Modified By:   James Rogers
Last Modified On:   01/06/2018
Purpose:            To detect if a door is open and send an email alert
'''

import RPi.GPIO as GPIO
import time

# Define pins that we are using
GREEN = 14
YELLOW = 15
RED = 18

# Enable BCM numbering and set input/outputs
GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

# Toggle LEDS on and off every second
while True:
    GPIO.output(GREEN, GPIO.HIGH)
    GPIO.output(YELLOW, GPIO.HIGH)
    GPIO.output(RED, GPIO.HIGH)
    time.sleep(1)

    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.LOW)
    time.sleep(1)

GPIO.cleanup()
