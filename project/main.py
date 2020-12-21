#!/usr/bin/env python

from time import sleep
from runner.independent_runner import IndependentRunner

runner = IndependentRunner()
runner.init()

while True:
    runner.step()
    sleep(0.1)

runner.shutdown()
