#!/usr/bin/env python

from project.data_types import IO
from project.common.heater import Heater


class Runner:
    def __init__(self, IOs):
        self.IOs = IOs
        self.input_data = dict.fromkeys(IOs.keys(), [])
        self.req_heater_state = False
        self.heater = Heater()

    def init(self):
        print("Initializing")

    def step(self):
        self.read_inputs()
        self.read_requests()

        if self.req_heater_state != self.heater.get_status():
            self.heater.set_status(self.req_heater_state)

        self.publish_commands()
        self.upload_outputs()

    def shutdown(self):
        print("Shutting Down")

    def read_inputs(self):
        pass

    def read_requests(self):
        pass

    def publish_commands(self):
        pass

    def upload_outputs(self):
        pass
