#!/usr/bin/env python
import random

class IOEmulator:
    def get_temperature(self):
        return random.uniform(0.0, 27.5)
    def get_heater_state(self):
        return bool(random.getrandbits(1))
