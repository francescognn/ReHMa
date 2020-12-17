#!/usr/bin/env python
from project.runner.runner import Runner


class AgnosticRunner(Runner):
        # db_emu = DbEmu()
        # raspberry_emu = RaspberryEmu()

    def read_inputs(self):
        # TODO: Add method to get agnostic input
        self.input_data_["TIN"] = 6.5
    
    def read_requests(self):
        # db_stub_.get_ignition_request()
        # self.req_heater_state = db_emu.get_heater_state() 
        self.req_heater_state = True 

    def publish_commands(self):
        # raspberry_emu.set_pin(["RELE"], True) 
        pass

    def upload_outputs(self):
        # db_emu.set_outputs(self.input_data_)
        pass
