#!/usr/bin/env python

from data_types import IO

class Runner:
    def Init(self):
        print("Initializing")
    def Step(self):
        man = self.update_input()
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
