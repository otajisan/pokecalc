import json
from pokecalc import input, calc, pokemon, nature


def test_calculation():
    """
    Dragapult

    [BS] H:88, A:120, B:75, C:100, D:75, S:142
    [EV] H:4, A: 252, S: 252
    [N] S:positive, D: negative

    [RV] H:164, A: 172, B:95, C: 120, D:85, S: 213

    :return:
    """
    expected = json.dumps({'h': 164, 'a': 172, 'b': 95, 'c': 120, 'd': 85, 's': 213})

    class Dragapult(pokemon.Pokemon):
        def __init__(self):
            super(Dragapult, self).__init__(_bs_h=88, _bs_a=120, _bs_b=75, _bs_c=100, _bs_d=75,
                                            _bs_s=142)

    p = Dragapult()
    n = nature.Naive()
    input_data = input.Input(
        _h=input.H(_ev=4),
        _a=input.A(_ev=252),
        _b=input.B(),
        _c=input.C(),
        _d=input.D(),
        _s=input.S(_ev=252)
    )

    actual = calc.calc(_pokemon=p, _nature=n, _input=input_data).to_json()

    assert actual == expected


def test_Talonflame():
    expected = json.dumps({'h': 153, 'a': 146, 'b': 92, 'c': 84, 'd': 89, 's': 178})

    class Talonflame(pokemon.Pokemon):
        def __init__(self):
            super(Talonflame, self).__init__(78, 81, 71, 74, 69, 126)

    assert calc.calc(
        _pokemon=Talonflame(),
        _nature=nature.Adamant(),
        _input=input.Input(
            _h=input.H(),
            _a=input.A(_ev=252),
            _b=input.B(_ev=4),
            _c=input.C(),
            _d=input.D(),
            _s=input.S(_ev=252)
        )
    ).to_json() == expected


def test_Porygon2():
    expected = json.dumps({'h': 191, 'a': 90, 'b': 156, 'c': 125, 'd': 115, 's': 82})

    class Porygon2(pokemon.Pokemon):
        def __init__(self):
            super(Porygon2, self).__init__(85, 80, 90, 105, 95, 60)

    assert calc.calc(
        _pokemon=Porygon2(),
        _nature=nature.Bold(),
        _input=input.Input(
            _h=input.H(_ev=244),
            _a=input.A(),
            _b=input.B(_ev=252),
            _c=input.C(),
            _d=input.D(),
            _s=input.S(_ev=12)
        )
    ).to_json() == expected
