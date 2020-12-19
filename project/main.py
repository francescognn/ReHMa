#!/usr/bin/env python

from time import sleep
from data_types import IO
from runner.independent_runner import IndependentRunner 

IOMapping = {
    "TIN": IO(1, "INPUT_PIN"),
    "TOUT": IO(2, "INPUT_PIN"),
    "RELE": IO(4, "OUTPUT_PIN"),
}

runner = IndependentRunner(IOMapping)
runner.init()

while True:
    runner.step()
    sleep(1)

runner.shutdown()
