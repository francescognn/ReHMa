#!/usr/bin/env python


class Heater:
    def __init__(self):
        self.__status = False

    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status
