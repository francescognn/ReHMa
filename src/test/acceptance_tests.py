#!/usr/bin/env python

import sys, unittest, time
from std_msgs.msg import *
import rospy, rostest
from src.test.utils.emulator import Emulator

PKG = 'project'
NAME = 'emulator_test'

class TestEmulator(unittest.TestCase):
    def __init__(self, *args):
        super(TestEmulator, self).__init__(*args)
        self.success = False
        
    def callback(self, data):
        self.success = data.data == 10.0

    def test_temperature(self):
        rospy.init_node(NAME, anonymous=True)
        rospy.Subscriber("temperature", Float64, self.callback)
        timeout_t = time.time() + 10.0 #10 seconds
        while not rospy.is_shutdown() and not self.success and time.time() < timeout_t:
            time.sleep(0.1)
        self.assert_(self.success)
        
if __name__ == '__main__':
    rostest.rosrun(PKG, NAME, TestEmulator, sys.argv)

