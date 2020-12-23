#!/usr/bin/env python

import unittest
import io
import sys
from src.runner.ros_runner import *
from src.test.utils.emulator import Emulator


class TestRosRunner(unittest.TestCase):
    def test_read_temperatures(self):
        runner = RosRunner()
        runner.read_temperatures()
        self.assertEqual(runner.temperatures["Sala"], 0.0)

    def test_read_heater_status(self):
        runner = RosRunner()
        self.assertFalse(runner.read_heater_status())

    def test_read_requests(self):
        runner = RosRunner()
        self.assertFalse(runner.read_requests())


if __name__ == "__main__":
    unittest.main()
