#!/usr/bin/env python

from src.test.utils.emulator import *

if __name__ == "__main__":
    try:
        heater_emulator = Emulator()
        heater_emulator.set_config("cycle")
        while not rospy.is_shutdown():
            heater_emulator.step()

    except rospy.ROSInterruptException:
        pass
