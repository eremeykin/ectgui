from normalization import Normalization


class Settings(object):

    def __init__(self):
        self.normalization = Normalization(Normalization.Center.NONE_CENTER,
                                           Normalization.Range.NONE_RANGE)
