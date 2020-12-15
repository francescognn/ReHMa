#!/usr/bin/env python

from time import sleep           # Allows us to call the sleep function to slow down our loop
import RPi.GPIO as GPIO           # Allows us to call our GPIO pins and names it just GPIO
 
GPIO.setmode(GPIO.BCM)           # Set's GPIO pins to BCM GPIO numbering
INPUT_PIN = 4           # Sets our input pin, in this example I'm connecting our button to pin 4. Pin 0 is the SDA pin so I avoid using it for sensors/buttons
GPIO.setup(INPUT_PIN, GPIO.IN)           # Set our input pin to be an input

# Start a loop that never ends
while True: 
           if (GPIO.input(INPUT_PIN) == True): # Physically read the pin now
                    print('3.3')
           else:
                    print('0')
           sleep(1);           # Sleep for a full second before restarting our loop

# Io creerei un runner che abbia un Init, una step e una shutdown functions e la creerei come classe virtuale, per poi avere due classi che ereditano da questa: 
    # - platform_runner (che userà librerie che possono girare solo su Raspberry per esempio GPIO) 
    # - agnostic_runner (che farà le stesse cose ma con interfacce stubbate, dovremmo quindi creare un generatore di reader e un writer)
# per quanto riguarda il testing io farei: 
    # - unit tests (che testano le singole funzioni), ne ho creato uno di esempio
    # - integration tests (test più completi che fanno girare tutto il codice simulando input e output

# Il platform_runner girerà sulla Raspberry mentre il agnostic_runner girerà solo per poter fare gli integration tests stubbundo input e output
