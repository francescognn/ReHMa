#!/usr/bin/env python

import unittest
import io
import sys
from core import Runner

class TestCoreMethods(unittest.TestCase):

    def test_init(self):
        runner = Runner()
        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput                   #  and redirect stdout.
        runner.Init()                                 # Call unchanged function.
        self.assertEqual(capturedOutput.getvalue(), "Initializing\n")
        sys.stdout = sys.__stdout__                   # Reset redirect.

    def test_step(self):
        runner = Runner()
        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput                   #  and redirect stdout.
        runner.Step()                                 # Call unchanged function.
        self.assertEqual(capturedOutput.getvalue(), "Step\n")
        sys.stdout = sys.__stdout__                   # Reset redirect.

    def test_shutdown(self):
        runner = Runner()
        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput                   #  and redirect stdout.
        runner.Shutdown()                                 # Call unchanged function.
        self.assertEqual(capturedOutput.getvalue(), "Shutting Down\n")
        sys.stdout = sys.__stdout__                   # Reset redirect.

