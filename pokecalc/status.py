import json


class Status:
    def __init__(self, _h, _a, _b, _c, _d, _s):
        self.h = _h
        self.a = _a
        self.b = _b
        self.c = _c
        self.d = _d
        self.s = _s

    def to_dict(self):
        return {
            'h': self.h,
            'a': self.a,
            'b': self.b,
            'c': self.c,
            'd': self.d,
            's': self.s,
        }

    def to_json(self):
        return json.dumps(self.to_dict())
