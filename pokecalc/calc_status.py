DEFAULT_EV = 0
DEFAULT_IV = MAX_IV = 31
DEFAULT_LV = 50

NATURE_POSITIVE = 1.1
NATURE_DEFAULT = 1.0
NATURE_NEGATIVE = 0.9


def h(bs, ev=DEFAULT_EV, iv=DEFAULT_IV, lv=DEFAULT_LV):
    validate_status(ev, iv, lv)
    status = (bs * 2 + iv + ev / 4) * lv / 100 + lv + 10

    return int(status)


def basic(bs, ev, iv, lv, n):
    validate_status(ev, iv, lv)
    status = ((bs * 2 + iv + ev / 4) * lv / 100 + 5) * n

    return int(status)


def a(bs, ev=DEFAULT_EV, iv=DEFAULT_IV, lv=DEFAULT_LV, n=NATURE_DEFAULT):
    return basic(bs, ev, iv, lv, n)


def b(bs, ev=DEFAULT_EV, iv=DEFAULT_IV, lv=DEFAULT_LV, n=NATURE_DEFAULT):
    return basic(bs, ev, iv, lv, n)


def c(bs, ev=DEFAULT_EV, iv=DEFAULT_IV, lv=DEFAULT_LV, n=NATURE_DEFAULT):
    return basic(bs, ev, iv, lv, n)


def d(bs, ev=DEFAULT_EV, iv=DEFAULT_IV, lv=DEFAULT_LV, n=NATURE_DEFAULT):
    return basic(bs, ev, iv, lv, n)


def s(bs, ev=DEFAULT_EV, iv=DEFAULT_IV, lv=DEFAULT_LV, n=NATURE_DEFAULT):
    return basic(bs, ev, iv, lv, n)


def validate_status(ev, iv, lv):
    if validate_lv(lv) is False:
        raise InvalidStatusError('invalid Level specified: %s', lv)
    if validate_ev(ev) is False:
        raise InvalidStatusError('invalid Effort Value specified: %s', ev)
    if validate_iv(iv) is False:
        raise InvalidStatusError('invalid Individual Value specified: %s', iv)


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


class InvalidStatusError(Exception):
    pass
