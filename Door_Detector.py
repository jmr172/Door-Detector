'''
Created By:         James Rogers
Last Modified By:   James Rogers
Last Modified On:   01/06/2018
Purpose:            To detect if a door is open and send an email alert
'''

import sys
import RPi.GPIO as GPIO
import time
import smtplib

if (len(sys.argv) != 2 or sys.argv[1] == "-h"):
    print("Usage: python3 Door_Detector.py to_address@example.com")
    sys.exit()

# Set to and from addresses
from_address = "door.detector.111@gmail.com"
to_address = sys.argv[1]

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

# Construct message to send
msg = "\r\n".join([
  "From: %s" % from_address,
  "To: %s" % to_address,
  "Subject: DOOR ALERT",
  "",
  "Your door is open."
  ])

# 0 if alert hasn't been sent, 1 if alert has already been sent
sent_email = 0

# DOOR_IN == 0 when door is open
while True:
    if (GPIO.input(DOOR_IN) == 0):
        # Amount of time for door to be open before alert is sent
        # Default is 30 seconds
        time.sleep(30)
        if (GPIO.input(DOOR_IN) == 0):
            if (sent_email != 1):
                # Setup smtp server as gmail
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(from_address, "doordetector111")
                server.sendmail(from_address, to_address, msg)
                server.quit()
                sent_email = 1
                print("Email sent")
    else:
        sent_email = 0
    time.sleep(1)

GPIO.cleanup()
