#!/usr/bin/env python

import unittest
import io
import sys
from project.data_types import IO
from project.runner.independent_runner import *
from project.common.heater import *
from project.test.utils.io_emulator import IOEmulator

IOMapping = {
    "TIN": IO(1, "INPUT_PIN"),
    "TOUT": IO(2, "INPUT_PIN"),
    "RELE": IO(4, "OUTPUT_PIN"),
}


class AcceptanceTests(unittest.TestCase):
    def test_remote_command(self):
        io_emulator = IOEmulator()
        io_emulator.set_config("trigger")
        runner = IndependentRunner(IOMapping, io_emulator)
        while runner.temperatures["Sala"] < 24.0:
            io_emulator.step()
            runner.step()
        self.assertEqual(runner.temperatures["Sala"], 24.0)

    def test_antifreeze(self):
        io_emulator = IOEmulator()
        io_emulator.set_config("antifreeze")
        runner = IndependentRunner(IOMapping, io_emulator)
        for x in range(20):
            io_emulator.step()
            runner.step()
            self.assertTrue(4.5 <= runner.temperatures["Sala"] <= 20)

    def test_constant(self):
        io_emulator = IOEmulator()
        io_emulator.set_config("constant")
        runner = IndependentRunner(IOMapping, io_emulator)
        io_emulator.step()
        runner.step()
        self.assertEqual(runner.temperatures["Sala"], 10.0)


if __name__ == "__main__":
    unittest.main()
