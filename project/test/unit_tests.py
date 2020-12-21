#!/usr/bin/env python

import unittest
import io
import sys
from project.runner.independent_runner import *
from project.test.utils.emulator import Emulator

class TestIndependentRunner(unittest.TestCase):

    def test_read_temperatures(self):
        runner = IndependentRunner()
        runner.read_temperatures()
        self.assertEqual(runner.temperatures["Sala"], 0.0)


if __name__ == "__main__":
    unittest.main()
