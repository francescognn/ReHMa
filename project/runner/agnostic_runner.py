#!/usr/bin/env python
from project.runner.runner import Runner
from project.common.db_emulator import DbEmulator


class AgnosticRunner(Runner):
    def __init__(self, IOs):
        Runner.__init__(self, IOs)
        self.db_emulator = DbEmulator()
        # raspberry_emu = RaspberryEmu()

    def read_inputs(self):
        self.input_data["TIN"] = 6.5

    def read_requests(self):
        self.req_heater_state = self.db_emulator.get_heater_state()
        self.req_heater_state = True

    def publish_commands(self):
        # raspberry_emu.set_pin(["RELE"], True)
        pass

    def upload_outputs(self):
        # db_emu.set_outputs(self.input_data_)
        pass
