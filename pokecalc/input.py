MAX_EV: int = 255
DEFAULT_EV: int = 0

MAX_IV: int = 31
DEFAULT_IV: int = MAX_IV

MAX_LEVEL: int = 100
DEFAULT_LV: int = 50


class InvalidInputError(Exception):
    pass


class Input:
    def __init__(self, _h, _a, _b, _c, _d, _s):
        check_input(_h, _a, _b, _c, _d, _s)
        self.h = _h
        self.a = _a
        self.b = _b
        self.c = _c
        self.d = _d
        self.s = _s


def check_input(h, a, b, c, d, s) -> bool:
    ev_sum = h.ev + a.ev + b.ev + c.ev + d.ev + s.ev
    if 510 < ev_sum:
        raise InvalidInputError('Effort Value over 510: %s', ev_sum)
    return True


def check_lv(lv) -> bool:
    if lv < 0 or MAX_LEVEL < lv:
        raise InvalidInputError('invalid Level specified: %s', lv)
    return True


def check_ev(ev) -> bool:
    if ev < 0 or MAX_EV < ev:
        raise InvalidInputError('invalid Effort Value specified: %s', ev)
    return True


def check_iv(iv) -> bool:
    if iv < 0 or MAX_IV < iv:
        raise InvalidInputError('invalid Individual Value specified: %s', iv)
    return True


def check_metadata(ev, iv, lv) -> bool:
    return check_lv(lv) and check_ev(ev) and check_iv(iv)


class MetaData:
    def __init__(self, _ev: int = DEFAULT_EV, _iv: int = DEFAULT_IV,
                 _lv: int = DEFAULT_LV):
        check_metadata(_ev, _iv, _lv)
        self.ev = _ev
        self.iv = _iv
        self.lv = _lv


class H(MetaData):
    pass


class A(MetaData):
    pass


class B(MetaData):
    pass


class C(MetaData):
    pass


class D(MetaData):
    pass


class S(MetaData):
    pass
