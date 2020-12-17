#!/usr/bin/env python
import random


class DbEmulator:
    def get_rand_heater_state(self):
        return bool(random.getrandbits(1))
