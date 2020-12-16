#!/usr/bin/env python

from data_types import IO

IOMap = {
IO("TIN", 1, "INPUT_PIN"),
IO("TOUT", 2, "INPUT_PIN"),
IO("RELE", 4, "OUTPUT_PIN"),
}

class Runner:
    def Init(self):
        print("Initializing")
    def Step(self):
        print("Step")
    def Shutdown(self):
        print("Shutting Down")
    # def get_input(self)
        
# class PlatformRunner(Runner):
    # def get_input(self):
        # return 1

# class AgnosticRunner(Runner):
    # def get_input(self):
        # return 2
