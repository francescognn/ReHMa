#!/usr/bin/env python

from time import sleep
from src.runner.ros_runner import RosRunner

runner = RosRunner()
runner.init()

while True:
    runner.step()
    sleep(0.1)

runner.shutdown()
