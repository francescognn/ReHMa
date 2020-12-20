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

    def step(self):
        if (self.heater_status == True):
            if self.current_temp <= T_MAX_HEATER:
                self.current_temp += 0.5
        else:
            if (self.config == "Winter"):
                if (self.current_temp > T_MIN):
                    self.current_temp -= 0.5 
            if (self.config == "Summer"):
                if (self.current_temp < T_MAX):
                    self.current_temp += 0.5

    def get_temperature(self):
        return self.current_temp 

    def get_heater_status(self):
        return self.heater_status 
    
    def set_heater_status(self, status):
        self.heater_status = status

    def set_config(self, config):
        self.config = config
