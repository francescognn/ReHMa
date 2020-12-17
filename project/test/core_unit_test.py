#!/usr/bin/env python

import unittest
import io
import sys
from project.data_types import IO
from project.runner.agnostic_runner import *
from project.common.heater import *

IOMapping = {
    "TIN": IO(1, "INPUT_PIN"),
    "TOUT": IO(2, "INPUT_PIN"),
    "RELE": IO(4, "OUTPUT_PIN"),
}


class TestCoreMethods(unittest.TestCase):
    def test_init(self):
        runner = AgnosticRunner(IOMapping)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        runner.init()
        self.assertEqual(capturedOutput.getvalue(), "Initializing\n")
        sys.stdout = sys.__stdout__

    def test_step(self):
        runner = AgnosticRunner(IOMapping)
        runner.step()
        self.assertEqual(runner.input_data_["TIN"], 6.5)
        self.assertEqual(runner.heater.get_status(), runner.req_heater_state)
        
    def test_shutdown(self):
        runner = AgnosticRunner(IOMapping)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        runner.shutdown()
        self.assertEqual(capturedOutput.getvalue(), "Shutting Down\n")
        sys.stdout = sys.__stdout__

    def test_read_input(self):
        runner = AgnosticRunner(IOMapping)
        runner.read_inputs()
        self.assertEqual(runner.input_data_["TIN"], 6.5)

class TestHeater(unittest.TestCase):
    def test_set_status(self):
        heater = Heater()
        heater.set_status(True)
        self.assertTrue(heater.get_status())

    def test_get_status(self):
        heater = Heater()
        self.assertFalse(heater.get_status())
