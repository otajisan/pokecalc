from pokecalc import calc_status


def test_calc():
    """
    Dragapult

    [IV] H:88, A:120, B:75, C:100, D:75, S:142
    [EV] H:4, A: 252, S: 252
    [N] S:positive, D: negative

    [RV] H:164, A: 172, B:95, C: 120, D:85, S: 213

    :return:
    """
    assert calc_status.h(bs=88, ev=4) == 164
    assert calc_status.a(bs=120, ev=252) == 172
    assert calc_status.b(bs=75, ev=0) == 95
    assert calc_status.c(bs=100, ev=0) == 120
    assert calc_status.d(bs=75, ev=0, n=calc_status.NATURE_NEGATIVE) == 85
    assert calc_status.s(bs=142, ev=252, n=calc_status.NATURE_POSITIVE) == 213
