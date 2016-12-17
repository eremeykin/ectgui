__author__ = 'eremeykin'
import collections


class Normalization(object):

        class Center(object):
            NoneCenter = -1
            Minimum = 0
            Mean = 2
            Median = 4
            MinkovskyCenter = 8

        class Range(object):
            NoneRange = -1
            Semirange = 0
            StandardDeviation = 2
            AbsoluteDeviation = 4

    def __init__(self, center, range):
        pass

    def normalize(self, data):
        result = data
        return result
