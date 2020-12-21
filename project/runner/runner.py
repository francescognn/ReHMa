#!/usr/bin/env python

from project.common.data_types import IO

class Runner:
    def __init__(self):
        self.temperatures = {"Sala": 0.0}
        self.current_heater_status = False
        self.req_heater_status = False
        self.antifreeze_mode = False

    def init(self):
        print("Initializing")

    def step(self):

        self.current_heater_status = self.read_heater_status()
        self.temperatures = self.read_temperatures()
        self.req_heater_status = self.read_requests()

        if self.req_heater_status != self.current_heater_status:
            self.publish_heater_command(self.req_heater_status)

        if self.temperatures["Sala"] < 5.0:
            self.publish_heater_command(True)
            self.antifreeze_mode = True
            print("Antifreeze ON")
        if (self.antifreeze_mode) and (self.temperatures["Sala"] > 7.0):
            self.publish_heater_command(False)
            self.antifreeze_mode = False

        self.upload_outputs()

    def shutdown(self):
        print("Shutting Down")

    def read_heater_status(self):
        pass

    def read_temperatures(self):
        pass

    def read_requests(self):
        pass

    def publish_heater_command(self):
        pass

    def upload_outputs(self):
        pass
