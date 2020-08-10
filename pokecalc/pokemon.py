from abc import ABCMeta


class Pokemon(metaclass=ABCMeta):
    def __init__(self, _bs_h, _bs_a, _bs_b, _bs_c, _bs_d, _bs_s):
        self.bs_h = _bs_h
        self.bs_a = _bs_a
        self.bs_b = _bs_b
        self.bs_c = _bs_c
        self.bs_d = _bs_d
        self.bs_s = _bs_s
