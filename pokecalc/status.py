DEFAULT_EV = 0
DEFAULT_IV = MAX_IV = 31
DEFAULT_LV = 50

NATURE_POSITIVE = 1.1
NATURE_DEFAULT = 1.0
NATURE_NEGATIVE = 0.9


def h(meta):
    return int((meta.bs * 2 + meta.iv + meta.ev / 4) * meta.lv / 100 + meta.lv + 10)


def basic(meta):
    return int(((meta.bs * 2 + meta.iv + meta.ev / 4) * meta.lv / 100 + 5) * meta.n)


def a(meta):
    return basic(meta)


def b(meta):
    return basic(meta)


def c(meta):
    return basic(meta)


def d(meta):
    return basic(meta)


def s(meta):
    return basic(meta)


class InvalidStatusError(Exception):
    pass


class Status:
    def __init__(self, _h, _a, _b, _c, _d, _s):
        self.h = _h
        self.a = _a
        self.b = _b
        self.c = _c
        self.d = _d
        self.s = _s

    def calc(self):
        return {
            'h': h(self.h),
            'a': a(self.a),
            'b': b(self.b),
            'c': c(self.c),
            'd': d(self.d),
            's': s(self.s),
        }


def validate_lv(lv):
    if lv < 0 or 100 < lv:
        return False
    return True


def validate_ev(ev):
    if ev < 0 or 255 < ev:
        return False
    return True


def validate_iv(iv):
    if iv < 0 or 31 < iv:
        return False
    return True


def validate_status(ev, iv, lv):
    if validate_lv(lv) is False:
        raise InvalidStatusError('invalid Level specified: %s', lv)
    if validate_ev(ev) is False:
        raise InvalidStatusError('invalid Effort Value specified: %s', ev)
    if validate_iv(iv) is False:
        raise InvalidStatusError('invalid Individual Value specified: %s', iv)


class MetaData:
    def __init__(self, _bs, _ev=DEFAULT_EV, _iv=DEFAULT_IV, _lv=DEFAULT_LV,
                 _n=NATURE_DEFAULT):
        validate_status(_ev, _iv, _lv)
        self.bs = _bs
        self.ev = _ev
        self.iv = _iv
        self.lv = _lv
        self.n = _n
