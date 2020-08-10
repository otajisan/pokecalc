MAX_EV: int = 255
DEFAULT_EV: int = 0

MAX_IV: int = 31
DEFAULT_IV: int = MAX_IV

MAX_LEVEL: int = 100
DEFAULT_LV: int = 50

NATURE_POSITIVE = 1.1
NATURE_DEFAULT = 1.0
NATURE_NEGATIVE = 0.9


def calc_status_hp(meta) -> int:
    return int((meta.bs * 2 + meta.iv + meta.ev / 4) * meta.lv / 100 + meta.lv + 10)


def calc_status(meta) -> int:
    return int(((meta.bs * 2 + meta.iv + meta.ev / 4) * meta.lv / 100 + 5) * meta.n)


class InvalidStatusError(Exception):
    pass


class Status:
    def __init__(self, _h, _a, _b, _c, _d, _s):
        check_status(_h, _a, _b, _c, _d, _s)
        self.h = _h
        self.a = _a
        self.b = _b
        self.c = _c
        self.d = _d
        self.s = _s

    def calc(self):
        return {
            'h': calc_status_hp(self.h),
            'a': calc_status(self.a),
            'b': calc_status(self.b),
            'c': calc_status(self.c),
            'd': calc_status(self.d),
            's': calc_status(self.s),
        }


def check_status(h, a, b, c, d, s) -> bool:
    ev_sum = h.ev + a.ev + b.ev + c.ev + d.ev + s.ev
    if 510 < ev_sum:
        raise InvalidStatusError('Effort Value over 510: %s', ev_sum)
    return True


def check_lv(lv) -> bool:
    if lv < 0 or MAX_LEVEL < lv:
        raise InvalidStatusError('invalid Level specified: %s', lv)
    return True


def check_ev(ev) -> bool:
    if ev < 0 or MAX_EV < ev:
        raise InvalidStatusError('invalid Effort Value specified: %s', ev)
    return True


def check_iv(iv) -> bool:
    if iv < 0 or MAX_IV < iv:
        raise InvalidStatusError('invalid Individual Value specified: %s', iv)
    return True


def check_metadata(ev, iv, lv) -> bool:
    return check_lv(lv) and check_ev(ev) and check_iv(iv)


class MetaData:
    def __init__(self, _bs: int, _ev: int = DEFAULT_EV, _iv: int = DEFAULT_IV,
                 _lv: int = DEFAULT_LV,
                 _n: int = NATURE_DEFAULT):
        check_metadata(_ev, _iv, _lv)
        self.bs = _bs
        self.ev = _ev
        self.iv = _iv
        self.lv = _lv
        self.n = _n


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
