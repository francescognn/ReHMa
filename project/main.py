#!/usr/bin/env python

from time import sleep
from data_types import IO
from runner.independent_runner import IndependentRunner 
from project.test.utils.io_emulator import IOEmulator

IOMapping = {
    "TIN": IO(1, "INPUT_PIN"),
    "TOUT": IO(2, "INPUT_PIN"),
    "RELE": IO(4, "OUTPUT_PIN"),
}
io_emulator = IOEmulator()
runner = IndependentRunner(IOMapping, io_emulator)
runner.init()
io_emulator.set_config("trigger")

while True:
    runner.step()
    io_emulator.step()
    sleep(0.2)

runner.shutdown()
