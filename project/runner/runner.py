#!/usr/bin/env python

from project.data_types import IO
from project.common.heater import Heater


class Runner:
    def __init__(self, IOs):
        self.IOs = IOs
        self.temperatures = {"Sala": 0.0}
        self.req_heater_state = False
        self.heater = Heater()
        self.antifreeze_mode = False

    def init(self):
        print("Initializing")

    def step(self):
        self.read_temperatures()
        self.read_requests()
        print("Temperature: ", self.temperatures["Sala"])
        print("Heater initial status: ", self.heater.get_status())
        if (self.req_heater_state != self.heater.get_status()):
            self.heater.set_status(self.req_heater_state)
        
        if (self.temperatures["Sala"] <= 5.0) :
            self.heater.set_status(True)
            self.antifreeze_mode = True
        
        if (self.antifreeze_mode) and (self.temperatures["Sala"] >= 7.0):
            self.heater.set_status(False)
            self.antifreeze_mode = False
        print("Heater final status: ", self.heater.get_status())
            
        self.publish_commands()
        self.upload_outputs()

    def shutdown(self):
        print("Shutting Down")

    def read_temperatures(self):
        pass

    def read_requests(self):
        pass

    def publish_commands(self):
        pass

    def upload_outputs(self):
        pass
