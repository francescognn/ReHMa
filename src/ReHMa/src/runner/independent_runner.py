#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool, Float64
from src.runner.runner import Runner


class IndependentRunner(Runner):
    def __init__(self):
        Runner.__init__(self)
        self.ros_heater_status = False
        self.ros_temperatures = {"Sala": 0.0}
        self.ros_remote_request = False

    
    def init(self):
        Runner.init(self)
        self.sub_temperature = rospy.Subscriber(
            "temperature", Float64, self.temperature_callback
        )
        self.sub_heater = rospy.Subscriber(
            "heater_status", Bool, self.heater_status_callback
        )
        self.sub_remote_request = rospy.Subscriber(
            "remote_request", Bool, self.remote_request_callback
        )
        self.pub_heater_command = rospy.Publisher("heater_command", Bool, queue_size=10)

        rospy.init_node("Runner", anonymous=True)
        self.rate = rospy.Rate(10)  # 10hz

    
    def read_temperatures(self):
        return self.ros_temperatures

    def read_heater_status(self):
        return self.ros_heater_status

    def read_requests(self):
        return self.ros_remote_request

    def publish_heater_command(self, command):
        self.pub_heater_command.publish(command)

    def upload_outputs(self):
        pass

    # Callbacks
    def temperature_callback(self, data):
        self.ros_temperatures["Sala"] = data.data

    def heater_status_callback(self, data):
        self.current_heater_status = data

    def remote_request_callback(self, data):
        self.ros_remote_request = data
    
    # Override with ros Step
    def step(self):
        Runner.step(self)
        # rospy.spin()
        self.rate.sleep()
