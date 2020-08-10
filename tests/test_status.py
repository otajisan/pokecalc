from pokecalc import status


def test_hp():
    """
    Dragapult

    [IV] H:88, A:120, B:75, C:100, D:75, S:142
    [EV] H:4, A: 252, S: 252
    [N] S:positive, D: negative

    [RV] H:164, A: 172, B:95, C: 120, D:85, S: 213

    :return:
    """
    assert status.h(bs=88, ev=4) == 164
    assert status.a(bs=120, ev=252) == 172
    assert status.b(bs=75, ev=0) == 95
    assert status.c(bs=100, ev=0) == 120
    assert status.d(bs=75, ev=0, n=status.NATURE_NEGATIVE) == 85
    assert status.s(bs=142, ev=252, n=status.NATURE_POSITIVE) == 213
