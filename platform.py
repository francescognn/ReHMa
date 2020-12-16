#!/usr/bin/env python

from time import sleep           # Allows us to call the sleep function to slow down our loop
import RPi.GPIO as GPIO           # Allows us to call our GPIO pins and names it just GPIO
from data_types import IO

GPIO.setmode(GPIO.BCM)           # Set's GPIO pins to BCM GPIO numbering
INPUT_PIN = 4           # Sets our input pin, in this example I'm connecting our button to pin 4. Pin 0 is the SDA pin so I avoid using it for sensors/buttons
GPIO.setup(INPUT_PIN, GPIO.IN)           # Set our input pin to be an input

IOMapping = {
  "TIN":  IO(1, "INPUT_PIN"),
  "TOUT": IO(2, "INPUT_PIN"),
  "RELE": IO(4, "OUTPUT_PIN")
}

# Start a loop that never ends
while True: 
           if (GPIO.input(INPUT_PIN) == True): # Physically read the pin now
                    print('3.3')
           else:
                    print('0')
           sleep(1);           # Sleep for a full second before restarting our loop

