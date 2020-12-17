#!/usr/bin/env python

from time import sleep
from data_types import IO
from runner.agnostic_runner import AgnosticRunner

IOMapping = {
    "TIN": IO(1, "INPUT_PIN"),
    "TOUT": IO(2, "INPUT_PIN"),
    "RELE": IO(4, "OUTPUT_PIN"),
}

runner = AgnosticRunner(IOMapping)
runner.Init()

while True:
    runner.Step()
    sleep(1)

runner.Shutdown()
