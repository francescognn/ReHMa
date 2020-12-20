#!/usr/bin/env python
from project.runner.runner import Runner


class IndependentRunner(Runner):
    def __init__(self, IOs, emulator):
        Runner.__init__(self, IOs)
        self.io_emulator = emulator

    def read_temperatures(self):
        self.temperatures["Sala"] = self.io_emulator.get_temperature()

    def read_heater_status(self):
        return self.io_emulator.get_heater_status() 
    
    def read_requests(self):
        self.req_heater_status = self.io_emulator.get_remote_request()

    def publish_heater_command(self, command):
        self.io_emulator.set_heater_status(command)

    def upload_outputs(self):
        # db_emu.set_outputs(self.input_data_)
        pass
