#!/usr/bin/env python
import random
import rospy
from std_msgs.msg import Bool, Float64

global T_MIN
global T_MAX
global T_MAX_HEATER

T_MIN = 2.0
T_MAX = 24.0


class Emulator:
    def __init__(self):
        self.heater_status = False
        self.current_temp = 10.0
        self.config = "constant"
        self.remote_request = False

        self.sub_heater_command = rospy.Subscriber(
            "heater_command", Bool, self.heater_command_callback
        )
        self.pub_heater_status = rospy.Publisher("heater_status", Bool, queue_size=10)
        self.pub_temperature = rospy.Publisher("temperature", Float64, queue_size=10)
        self.pub_remote_request = rospy.Publisher("remote_request", Bool, queue_size=10)

        rospy.init_node("emulator", anonymous=True)
        self.rate = rospy.Rate(10)  # 10hz

    def step(self):
        if self.config == "summer":
            if self.current_temp < T_MAX:
                self.current_temp += 0.05

        if self.config == "constant":
            pass

        if self.config == "winter":
            if self.current_temp > T_MIN:
                self.current_temp -= 0.05

        if self.heater_status and self.current_temp <= T_MAX:
            self.current_temp += 0.1

        self.pub_heater_status.publish(self.heater_status)
        self.pub_temperature.publish(self.current_temp)
        self.rate.sleep()

    def heater_command_callback(self, data):
        self.heater_status = data.data

    def set_config(self, config):
        self.config = config


if __name__ == "__main__":
    try:
        heater_emulator = Emulator()
        heater_emulator.set_config("winter")

        while not rospy.is_shutdown():
            heater_emulator.step()

    except rospy.ROSInterruptException:
        pass
