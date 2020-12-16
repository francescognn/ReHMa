#!/usr/bin/env python

from time import sleep
from runner import Runner

runner = Runner()
runner.Init()

while True: 
    runner.Step()       
    sleep(1)

runner.Shutdown()

