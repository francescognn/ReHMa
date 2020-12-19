#!/usr/bin/env python

import unittest
import io
import sys
from project.data_types import IO
from project.runner.independent_runner import *
from project.common.heater import *
from project.common.raspberry_emulator import RaspberryEmulator

IOMapping = {
    "TIN": IO(1, "INPUT_PIN"),
    "TOUT": IO(2, "INPUT_PIN"),
    "RELE": IO(4, "OUTPUT_PIN"),
}


class TestCoreMethods(unittest.TestCase):
    def test_init(self):
        runner = IndependentRunner(IOMapping)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        runner.init()
        self.assertEqual(capturedOutput.getvalue(), "Initializing\n")
        sys.stdout = sys.__stdout__

    def test_step(self):
        runner = IndependentRunner(IOMapping)
        runner.step()
        self.assertTrue(0.0 <= runner.temperatures["Sala"] <= 27.5)
        self.assertEqual(runner.heater.get_status(), runner.req_heater_state)

    def test_shutdown(self):
        runner = IndependentRunner(IOMapping)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        runner.shutdown()
        self.assertEqual(capturedOutput.getvalue(), "Shutting Down\n")
        sys.stdout = sys.__stdout__

    def test_read_temperatures(self):
        runner = IndependentRunner(IOMapping)
        runner.read_temperatures()
        self.assertTrue(0.0 <= runner.temperatures["Sala"] <= 27.5)


class TestHeater(unittest.TestCase):
    def test_set_status(self):
        heater = Heater()
        heater.set_status(True)
        self.assertTrue(heater.get_status())

    def test_get_status(self):
        heater = Heater()
        self.assertFalse(heater.get_status())


class TestRaspberryEmulator(unittest.TestCase):
    def test_get_rand_temperature(self):
        raspberry_emulator = RaspberryEmulator()
        self.assertTrue(0.0 <= raspberry_emulator.get_rand_temperature() <= 27.5)
