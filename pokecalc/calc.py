from pokecalc import status


def calc_status_hp(bs, meta) -> int:
    return int((bs * 2 + meta.iv + meta.ev / 4) * meta.lv / 100 + meta.lv + 10)


def calc_status(bs, n, meta) -> int:
    return int(((bs * 2 + meta.iv + meta.ev / 4) * meta.lv / 100 + 5) * n)


def calc(_pokemon, _nature, _input):
    return status.Status(
        _h=calc_status_hp(_pokemon.bs_h, _input.h),
        _a=calc_status(_pokemon.bs_a, _nature.a, _input.a),
        _b=calc_status(_pokemon.bs_b, _nature.b, _input.b),
        _c=calc_status(_pokemon.bs_c, _nature.c, _input.c),
        _d=calc_status(_pokemon.bs_d, _nature.d, _input.d),
        _s=calc_status(_pokemon.bs_s, _nature.s, _input.s),
    )
