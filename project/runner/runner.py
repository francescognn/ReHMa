#!/usr/bin/env python

from project.data_types import IO


class Runner:
    def __init__(self, IOs):
        self.IOs = IOs
        self.input_data = dict.fromkeys(IOs.keys(), [])

    def Init(self):
        print("Initializing")
        self.update_input()

    def Step(self):
        print("Step")

    def Shutdown(self):
        print("Shutting Down")

    def update_input(self):
        pass
