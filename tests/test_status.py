from pokecalc import status


def test_raw_layer_calculation():
    """
    Dragapult

    [IV] H:88, A:120, B:75, C:100, D:75, S:142
    [EV] H:4, A: 252, S: 252
    [N] S:positive, D: negative

    [RV] H:164, A: 172, B:95, C: 120, D:85, S: 213

    :return:
    """
    assert status.h(status.MetaData(_bs=88, _ev=4)) == 164
    assert status.a(status.MetaData(_bs=120, _ev=252)) == 172
    assert status.b(status.MetaData(_bs=75, _ev=0)) == 95
    assert status.c(status.MetaData(_bs=100, _ev=0)) == 120
    assert status.d(status.MetaData(_bs=75, _ev=0, _n=status.NATURE_NEGATIVE)) == 85
    assert status.s(status.MetaData(_bs=142, _ev=252, _n=status.NATURE_POSITIVE)) == 213


def test_high_layer_calculation():
    """
    Dragapult

    [IV] H:88, A:120, B:75, C:100, D:75, S:142
    [EV] H:4, A: 252, S: 252
    [N] S:positive, D: negative

    [RV] H:164, A: 172, B:95, C: 120, D:85, S: 213

    :return:
    """
    expected = {'h': 164, 'a': 172, 'b': 95, 'c': 120, 'd': 85, 's': 213}
    st = status.Status(
        _h=status.MetaData(_bs=88, _ev=4),
        _a=status.MetaData(_bs=120, _ev=252),
        _b=status.MetaData(_bs=75),
        _c=status.MetaData(_bs=100),
        _d=status.MetaData(_bs=75, _n=status.NATURE_NEGATIVE),
        _s=status.MetaData(_bs=142, _ev=252, _n=status.NATURE_POSITIVE)
    )

    actual = st.calc()

    assert actual == expected
