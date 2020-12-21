#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool, Float64
from project.runner.runner import Runner


class IndependentRunner(Runner):
    def __init__(self, IOs):
        Runner.__init__(self, IOs)
        self.sub_heater = rospy.Subscriber("heater_status", Bool, self.heater_status_callback)
        self.sub_temperature = rospy.Subscriber("temperature", Float64, self.temperature_callback)
        rospy.init_node('Runner', anonymous=True)
        self.rate = rospy.Rate(10) # 10hz
        self.ros_heater_status = False
        self.ros_temperatures = {"Sala": 0.0}
    
    def temperature_callback(self, data):
        self.ros_temperatures["Sala"] = data
        rospy.loginfo(data)    

    def heater_status_callback(self, data):
        self.current_heater_status = data
        rospy.loginfo(data)
        
    def read_temperatures(self):
        self.temperatures = self.ros_temperatures 

    def read_heater_status(self):
        self.current_heater_status = self.ros_heater_status

    def read_requests(self):
        self.req_heater_status = False

    def publish_heater_command(self, command):
        pass

    def upload_outputs(self):
        # db_emu.set_outputs(self.input_data_)
        pass

    def step(self):
        Runner.step(self)
        rospy.spin()

