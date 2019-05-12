"""
With this, everyone can create a tone.
"""

import math


class ToneGenerator:
    """
    With this, everyone can create a tone.
    """

    def __init__(self, fs, f):
        """
        Tone generator.
        Parameters:
        fs - sampling frequency
        f - frequency
        """
        self.__fs = fs
        self.__f = f
        self.__phasak = 0
        self.__maxint = 4294967295
        self.__hz = self.__maxint / self.__fs

    def output(self):
        """
        Takes one step and outputs new value.
        """
        self.__phasak = self.__phasak + self.__f * self.__hz
        self.__phasak = self.__phasak % self.__maxint
        return math.cos(2*math.pi*self.__phasak/self.__maxint)*100
