#!/usr/bin/env python

import sys, unittest, time
from std_msgs.msg import *
import rospy, rostest
from src.test.utils.emulator import Emulator

PKG = "project"
NAME = "emulator_test"


class TestEmulator(unittest.TestCase):
    def __init__(self, *args):
        super(TestEmulator, self).__init__(*args)
        self.success = False

    def callback_temperature(self, data):
        self.success_temperature = data.data >= 4.5

    def callback_status(self, data):
        self.success_status = data.data == True

    def test_temperature(self):
        rospy.init_node(NAME, anonymous=True)
        rospy.Subscriber("temperature", Float64, self.callback_temperature)
        rospy.Subscriber("heater_status", Bool, self.callback_status)
        timeout_t = time.time() + 22.0
        start_time = time.time()
        while not rospy.is_shutdown() and not self.success and time.time() < timeout_t:
            time.sleep(0.1)
            self.assertTrue(self.success_temperature)
        self.assertTrue(self.success_status)

if __name__ == "__main__":
    rostest.rosrun(PKG, NAME, TestEmulator, sys.argv)
