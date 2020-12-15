#!/usr/bin/env python

from time import sleep           # Allows us to call the sleep function to slow down our loop
from core import Runner           # Allows us to call the sleep function to slow down our loop

runner = Runner()
runner.Init()

while True: 
    runner.Step()       
    sleep(1);           # Sleep for a full second before restarting our loop

runner.Shutdown()

