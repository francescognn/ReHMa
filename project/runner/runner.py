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

        self.read_heater_status()
        self.read_temperatures()
        self.read_requests()

        print("Temperature: ", self.temperatures["Sala"])
        if self.req_heater_status != self.read_heater_status():
            self.publish_heater_command(self.req_heater_status)

        if self.temperatures["Sala"] < 5.0:
            self.publish_heater_command(True)
            self.antifreeze_mode = True

        if (self.antifreeze_mode) and (self.temperatures["Sala"] > 7.0):
            self.publish_heater_command(False)
            self.antifreeze_mode = False

        print("Heater status: ", self.read_heater_status())

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
