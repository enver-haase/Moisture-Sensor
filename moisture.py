#!/usr/bin/python3

# Start by importing the libraries we want to use

import RPi.GPIO as GPIO # This is the GPIO library we need to use the GPIO pins on the Raspberry Pi
import time # This is the time library, we need this so we can use the sleep function

# Define some variables to be used later on in our script


# This is our callback function, this function will be called every time there is a change on the specified GPIO channel, in this example we are using 17
def callback(channel):
	wet = GPIO.input(channel_moisture_wet)
	dry = GPIO.input(channel_moisture_dry)
	if dry == 1 and wet == 1:
		print ("TOO DRY")
		GPIO.output(channel_led_bad, GPIO.HIGH)
	if dry == 1 and wet == 0:
		print ("SYSTEM ERROR")
		GPIO.output(channel_led_bad, GPIO.HIGH)
	if dry == 0 and wet == 1:
		print ("IN A GOOD RANGE")
		GPIO.output(channel_led_bad, GPIO.LOW)
	if dry == 0 and wet == 0:
		print ("TOO WET")
		GPIO.output(channel_led_bad, GPIO.HIGH)

# Remove warnings for already used GPIOs (why do they show? Everything just works fine.)
GPIO.setwarnings(False)

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that we have our digital output from our sensor connected to
channel_moisture_wet = 17
channel_moisture_dry = 18
channel_led_good = 5
channel_led_bad = 6
# Set the GPIO pin to an input
GPIO.setup(channel_moisture_wet, GPIO.IN)
GPIO.setup(channel_moisture_dry, GPIO.IN)
GPIO.setup(channel_led_good, GPIO.OUT)
GPIO.setup(channel_led_bad, GPIO.OUT)

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel_moisture_wet, GPIO.BOTH)
GPIO.add_event_detect(channel_moisture_dry, GPIO.BOTH)
# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
GPIO.add_event_callback(channel_moisture_wet, callback)
GPIO.add_event_callback(channel_moisture_dry, callback)

callback(channel_moisture_dry) # initialize 'bad' LED
# This is an infinte loop to keep our script running
while True:
	# This line simply tells our script to wait 0.5 of a second, this is so the script doesnt hog all of the CPU
	time.sleep(0.5)
	#GPIO.output(channel_led_bad, GPIO.LOW)
	#time.sleep(0.5)
	#GPIO.output(channel_led_bad, GPIO.HIGH)
