#!/usr/bin/env python

from data_types import IO

class Runner:

    def __init__(self, IOs):
        self.input_data = dict.fromkeys(IOs.keys(),[])

    def Init(self):
        print("Initializing")
        self.update_input()
    def Step(self):
        print("Step")
    def Shutdown(self):
        print("Shutting Down")
    def update_input(self):
        pass

# class PlatformRunner(Runner):
    # def get_input(self):
        # return 1

class AgnosticRunner(Runner):
    def update_input(self):
        return 2
