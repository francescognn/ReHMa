#!/usr/bin/env python

import unittest
import io
import sys
from runner import AgnosticRunner
from data_types import IO

IOMapping = {
  "TIN":  IO(1, "INPUT_PIN"),
  "TOUT": IO(2, "INPUT_PIN"),
  "RELE": IO(4, "OUTPUT_PIN")
}

class TestCoreMethods(unittest.TestCase):

    def test_init(self):
        runner = AgnosticRunner(IOMapping)
        capturedOutput = io.StringIO()        
        sys.stdout = capturedOutput
        runner.Init()
        self.assertEqual(capturedOutput.getvalue(), "Initializing\n")
        sys.stdout = sys.__stdout__

    def test_step(self):
        runner = AgnosticRunner(IOMapping)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        runner.Step()
        self.assertEqual(capturedOutput.getvalue(), "Step\n")
        sys.stdout = sys.__stdout__

    def test_shutdown(self):
        runner = AgnosticRunner(IOMapping)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        runner.Shutdown()
        self.assertEqual(capturedOutput.getvalue(), "Shutting Down\n")
        sys.stdout = sys.__stdout__
    
    def test_update_input(self):
        runner = AgnosticRunner(IOMapping)
        self.assertEqual(runner.update_input(), 2) 
