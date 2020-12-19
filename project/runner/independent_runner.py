#!/usr/bin/env python
from project.runner.runner import Runner
from project.test.utils.io_emulator import IOEmulator


class IndependentRunner(Runner):
    def __init__(self, IOs):
        Runner.__init__(self, IOs)
        self.io_emulator = IOEmulator()

    def read_temperatures(self):
        self.temperatures["Sala"] = self.io_emulator.get_temperature()

    def read_requests(self):
        self.req_heater_state = self.io_emulator.get_heater_state()

    def publish_commands(self):
        # raspberry_emu.set_pin(["RELE"], True)
        pass

    def upload_outputs(self):
        # db_emu.set_outputs(self.input_data_)
        pass
