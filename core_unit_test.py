#!/usr/bin/env python

import unittest
import io
import sys
from runner import Runner

class TestCoreMethods(unittest.TestCase):

    def test_init(self):
        runner = Runner()
        capturedOutput = io.StringIO()        
        sys.stdout = capturedOutput
        runner.Init()
        self.assertEqual(capturedOutput.getvalue(), "Initializing\n")
        sys.stdout = sys.__stdout__

    def test_step(self):
        runner = Runner()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        runner.Step()
        self.assertEqual(capturedOutput.getvalue(), "Step\n")
        sys.stdout = sys.__stdout__

    def test_shutdown(self):
        runner = Runner()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        runner.Shutdown()
        self.assertEqual(capturedOutput.getvalue(), "Shutting Down\n")
        sys.stdout = sys.__stdout__

