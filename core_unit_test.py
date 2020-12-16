#!/usr/bin/env python

import unittest
import io
import sys
from runner import AgnosticRunner

class TestCoreMethods(unittest.TestCase):

    def test_init(self):
        runner = AgnosticRunner()
        capturedOutput = io.StringIO()        
        sys.stdout = capturedOutput
        runner.Init()
        self.assertEqual(capturedOutput.getvalue(), "Initializing\n")
        sys.stdout = sys.__stdout__

    def test_step(self):
        runner = AgnosticRunner()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        runner.Step()
        self.assertEqual(capturedOutput.getvalue(), "Step\n")
        sys.stdout = sys.__stdout__

    def test_shutdown(self):
        runner = AgnosticRunner()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        runner.Shutdown()
        self.assertEqual(capturedOutput.getvalue(), "Shutting Down\n")
        sys.stdout = sys.__stdout__
    
    def test_update_input(self):
        runner = AgnosticRunner()
        self.assertEqual(runner.update_input(), 2) 
