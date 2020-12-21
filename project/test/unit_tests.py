#!/usr/bin/env python

import unittest
import io
import sys
from project.common.data_types import IO
from project.runner.independent_runner import *
from project.test.utils.io_emulator import IOEmulator

IOMapping = {
    "TIN": IO(1, "INPUT_PIN"),
    "TOUT": IO(2, "INPUT_PIN"),
    "RELE": IO(4, "OUTPUT_PIN"),
}


class TestCoreMethods(unittest.TestCase):
    def test_init(self):
        io_emulator = IOEmulator()
        runner = IndependentRunner(IOMapping, io_emulator)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        runner.init()
        self.assertEqual(capturedOutput.getvalue(), "Initializing\n")
        sys.stdout = sys.__stdout__

    def test_step(self):
        io_emulator = IOEmulator()
        runner = IndependentRunner(IOMapping, io_emulator)
        runner.step()
        self.assertTrue(0.0 <= runner.temperatures["Sala"] <= 27.5)
        self.assertEqual(runner.read_heater_status(), runner.req_heater_state)

    def test_shutdown(self):
        io_emulator = IOEmulator()
        runner = IndependentRunner(IOMapping, io_emulator)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        runner.shutdown()
        self.assertEqual(capturedOutput.getvalue(), "Shutting Down\n")
        sys.stdout = sys.__stdout__

    def test_read_temperatures(self):
        io_emulator = IOEmulator()
        runner = IndependentRunner(IOMapping, io_emulator)
        runner.read_temperatures()
        self.assertTrue(0.0 <= runner.temperatures["Sala"] <= 27.5)


if __name__ == "__main__":
    unittest.main()
