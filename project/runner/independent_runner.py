#!/usr/bin/env python
from project.runner.runner import Runner
from project.common.db_emulator import DbEmulator
from project.common.raspberry_emulator import RaspberryEmulator


class IndependentRunner(Runner):
    def __init__(self, IOs):
        Runner.__init__(self, IOs)
        self.db_emulator = DbEmulator()
        self.raspberry_emulator = RaspberryEmulator()

    def read_temperatures(self):
        self.temperatures["Sala"] = self.raspberry_emulator.get_rand_temperature()

    def read_requests(self):
        self.req_heater_state = self.db_emulator.get_rand_heater_state()

    def publish_commands(self):
        # raspberry_emu.set_pin(["RELE"], True)
        pass

    def upload_outputs(self):
        # db_emu.set_outputs(self.input_data_)
        pass
