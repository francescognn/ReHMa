#!/usr/bin/env python

import unittest
import io
import sys
from src.runner.independent_runner import *
from src.test.utils.emulator import Emulator


class TestIndependentRunner(unittest.TestCase):
    def test_read_temperatures(self):
        runner = IndependentRunner()
        runner.read_temperatures()
        self.assertEqual(runner.temperatures["Sala"], 0.0)

    def test_read_heater_status(self):
        runner = IndependentRunner()
        self.assertFalse(runner.read_heater_status())

    def test_read_requests(self):
        runner = IndependentRunner()
        self.assertFalse(runner.read_requests())


if __name__ == "__main__":
    unittest.main()
