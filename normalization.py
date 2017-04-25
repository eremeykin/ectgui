__author__ = 'eremeykin'
from collections import namedtuple

import numpy as np
import pandas as pd
from scipy.optimize import fmin_tnc


class Normalization(object):
    class Type(object):
        @classmethod
        def all(cls):
            c = cls
            return [getattr(c, attr) for attr in dir(c) if not callable(getattr(c, attr)) and not attr.startswith("__")]

        @classmethod
        def get(cls, name):
            for item in cls.all():
                if item.name == name:
                    return item
            raise Exception('Unknown Type: ' + str(name))

    class Center(Type):
        CenterType = namedtuple('CenterType', 'value name')
        NONE_CENTER = CenterType(0, 'No centring')
        MINIMUM = CenterType(2 ** 1, 'Minimum')
        MEAN = CenterType(2 ** 3, 'Mean')
        MEDIAN = CenterType(2 ** 3, 'Median')
        MINKOWSKI_CENTER = CenterType(2 ** 4, 'Minkowski center')

    class Range(Type):
        RangeType = namedtuple('RangeType', 'value name')
        NONE_RANGE = RangeType(2 ** 5, 'None range')
        SEMI_RANGE = RangeType(2 ** 6, 'Semi range')
        STANDARD_DEVIATION = RangeType(2 ** 7, 'Standard deviation')
        ABSOLUTE_DEVIATION = RangeType(2 ** 8, 'Absolute deviation')

    def __init__(self, center, range, enabled=False, p=None):
        self.center_type = center
        self.range_type = range
        self.enabled = enabled
        self.p = p
        if self.center_type == Normalization.Center.MINKOWSKI_CENTER and self.p is None:
            raise Exception('p (power) is required for minkowski center calculation')
        self.rng = None
        self.center = None

    def apply(self, data):
        if not self.enabled:
            return data
        if isinstance(data, pd.Series):
            return self._apply(data)
        if isinstance(data, pd.DataFrame):
            return data.apply(lambda x: self._apply(x))

        raise Exception('Wrong data type for normalization')

    def apply_reverse(self, real_data,norm_data, centroids):
        if isinstance(real_data, pd.Series):
            return self._apply_reverse(self.data, centroids[0])
        if isinstance(real_data, pd.DataFrame):
            res = np.empty((centroids.shape[0], 0))
            for c,column in enumerate(norm_data):
                series = real_data[column]
                reversed = self._apply_reverse(series, centroids[:,c])
                res = np.hstack((res, reversed.reshape(centroids.shape[0], 1)))
            return res
        raise Exception('Wrong data type for denormalization')

    def _apply_reverse(self, series, c):
        c = c.reshape((c.shape[0],1))
        center = self._get_center(series)
        rng = self._get_rng(series)
        result = c * rng + center
        return result

    def _get_center(self, series):
        if self.center_type == Normalization.Center.NONE_CENTER:
            center = 0
        elif self.center_type == Normalization.Center.MINIMUM:
            center = series.min()
        elif self.center_type == Normalization.Center.MEAN:
            center = series.mean()
        elif self.center_type == Normalization.Center.MEDIAN:
            center = series.median()
        elif self.center_type == Normalization.Center.MINKOWSKI_CENTER:
            def D(X, a):
                return np.sum(np.abs(X - a) ** self.p) / len(X)

            center = fmin_tnc(func=lambda x: D(series, x), x0=np.mean(series), approx_grad=True)[0]
        else:
            raise Exception('Unknown center type')
        return center

    def _get_rng(self, series):
        if self.range_type == Normalization.Range.NONE_RANGE:
            rng = 1
        elif self.range_type == Normalization.Range.SEMI_RANGE:
            rng = (series.max() - series.min()) / 2
        elif self.range_type == Normalization.Range.STANDARD_DEVIATION:
            rng = series.std()
        elif self.range_type == Normalization.Range.ABSOLUTE_DEVIATION:
            rng = ((series - series.median()).abs()).mean()
        else:
            raise Exception('Unknown range type')
        return rng

    def _apply(self, series):
        center = self._get_center(series)
        rng = self._get_rng(series)
        result = (series - center) / rng
        return result

    def __bool__(self):
        return True

    def center_str(self):
        if not self.enabled:
            return 'normalization disabled'
        return 'center: ' + str(self.center_type[1])

    def range_str(self):
        if not self.enabled:
            return 'normalization disabled'
        res = 'range: ' + str(self.range_type[1])
        if self.center_type == Normalization.Center.MINKOWSKI_CENTER:
            res += ' minkowski power: ' + str(self.p)
        return res

