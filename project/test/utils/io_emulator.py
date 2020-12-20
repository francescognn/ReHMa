#!/usr/bin/env python
import random

global T_MIN
global T_MAX
global T_MAX_HEATER

T_MIN = 2.0
T_MAX = 20.0
T_MAX_HEATER = 27.5


class IOEmulator:
    def __init__(self):
        self.heater_status = False
        self.current_temp = 10.0
        self.config = "Summer"
        self.flag = True
        self.iterator = 0
        self.remote_request = False

    def step(self):
        if self.config == "antifreeze":
            if self.heater_status == True:
                if self.current_temp < T_MAX_HEATER:
                    self.current_temp += 1
                if self.current_temp > 6.0:
                    self.flag = False
            if self.current_temp > T_MIN and self.flag:
                self.current_temp -= 0.5

        if self.config == "constant":
            if self.heater_status == True:
                if self.current_temp < T_MAX_HEATER:
                    self.current_temp += 0.5

        if self.config == "trigger":
            if self.heater_status == True:
                if self.current_temp < T_MAX_HEATER:
                    self.current_temp += 0.5
            if self.iterator == 5:
                self.remote_request = True
            self.iterator += 1

    def get_remote_request(self):
        return self.remote_request

    def get_temperature(self):
        return self.current_temp

    def get_heater_status(self):
        return self.heater_status

    def set_heater_status(self, status):
        self.heater_status = status

    def set_config(self, config):
        self.config = config
        if config == "antifreeze":
            self.current_temp = 6.0
