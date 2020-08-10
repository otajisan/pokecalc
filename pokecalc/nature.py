from abc import ABCMeta


class Nature(metaclass=ABCMeta):
    def __init__(self):
        self.a = 1.0
        self.b = 1.0
        self.c = 1.0
        self.d = 1.0
        self.s = 1.0


class Adamant(Nature):
    """いじっぱり"""

    def __init__(self):
        super(Adamant, self).__init__()
        self.a = 1.1
        self.c = 0.9


class Bashful(Nature):
    """てれや"""
    pass


class Bold(Nature):
    """ずぶとい"""

    def __init__(self):
        super(Bold, self).__init__()
        self.a = 0.9
        self.b = 1.1


class Brave(Nature):
    """ゆうかん"""

    def __init__(self):
        super(Brave, self).__init__()
        self.a = 1.1
        self.s = 0.9


class Calm(Nature):
    """おだやか"""

    def __init__(self):
        super(Calm, self).__init__()
        self.a = 0.9
        self.d = 1.1


class Careful(Nature):
    """しんちょう"""

    def __init__(self):
        super(Careful, self).__init__()
        self.c = 0.9
        self.d = 1.1


class Docile(Nature):
    """すなお"""
    pass


class Gentle(Nature):
    """おとなしい"""

    def __init__(self):
        super(Gentle, self).__init__()
        self.b = 0.9
        self.d = 1.1


class Hardy(Nature):
    """がんばりや"""
    pass


class Hasty(Nature):
    """せっかち"""

    def __init__(self):
        super(Hasty, self).__init__()
        self.b = 0.9
        self.s = 1.1


class Impish(Nature):
    """わんぱく"""

    def __init__(self):
        super(Impish, self).__init__()
        self.b = 1.1
        self.c = 0.9


class Jolly(Nature):
    """ようき"""

    def __init__(self):
        super(Jolly, self).__init__()
        self.c = 0.9
        self.s = 1.1


class Lax(Nature):
    """のうてんき"""

    def __init__(self):
        super(Lax, self).__init__()
        self.b = 1.1
        self.d = 0.9


class Lonely(Nature):
    """さみしがり"""

    def __init__(self):
        super(Lonely, self).__init__()
        self.a = 1.1
        self.b = 0.9


class Mild(Nature):
    """おっとり"""

    def __init__(self):
        super(Mild, self).__init__()
        self.b = 0.9
        self.c = 1.1


class Modest(Nature):
    """ひかえめ"""

    def __init__(self):
        super(Modest, self).__init__()
        self.a = 0.9
        self.c = 1.1


class Naive(Nature):
    """むじゃき"""

    def __init__(self):
        super(Naive, self).__init__()
        self.d = 0.9
        self.s = 1.1


class Naughty(Nature):
    """やんちゃ"""

    def __init__(self):
        super(Naughty, self).__init__()
        self.a = 1.1
        self.d = 0.9


class Quiet(Nature):
    """れいせい"""

    def __init__(self):
        super(Quiet, self).__init__()
        self.c = 1.1
        self.s = 0.9


class Quirky(Nature):
    """きまぐれ"""
    pass


class Rash(Nature):
    """うっかりや"""

    def __init__(self):
        super(Rash, self).__init__()
        self.c = 1.1
        self.d = 0.9


class Relaxed(Nature):
    """のんき"""

    def __init__(self):
        super(Relaxed, self).__init__()
        self.b = 1.1
        self.s = 0.9


class Sassy(Nature):
    """なまいき"""

    def __init__(self):
        super(Sassy, self).__init__()
        self.d = 1.1
        self.s = 0.9


class Serious(Nature):
    """まじめ"""
    pass


class Timid(Nature):
    """おくびょう"""

    def __init__(self):
        super(Timid, self).__init__()
        self.a = 0.9
        self.s = 1.1
