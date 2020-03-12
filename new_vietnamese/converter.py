import re

class Converter(object):
    def __init__(self, str):
        self.str = str
        self.maps = [
            ['k(h|H)', 'x'],
            ['K(h|H)', 'X'],
            ['c(?!(h|H))|q', 'k'],
            ['C(?!(h|H))|Q', 'K'],
            ['t(r|R)|c(h|H)', 'c'],
            ['T(r|R)|C(h|H)', 'C'],
            ['d|g(i|I)|r', 'z'],
            ['D|G(i|I)|R', 'Z'],
            ['g(i|ì|í|ỉ|ĩ|ị|I|Ì|Í|Ỉ|Ĩ|Ị)', r'z\1'],
            ['G(i|ì|í|ỉ|ĩ|ị|I|Ì|Í|Ỉ|Ĩ|Ị)', r'Z\1'],
            ['đ', 'd'],
            ['Đ', 'D'],
            ['p(h|H)', 'f'],
            ['P(h|H)', 'F'],
            ['n(g|G)(h|H)?', 'q'],
            ['N(g|G)(h|H)?', 'Q'],
            ['(g|G)(h|H)', 'g'],
            ['t(h|H)', 'w'],
            ['T(h|H)', 'W'],
            ['(n|N)(h|H)', 'n\'']
        ]

    def convert(self):
        for map in self.maps:
            self.str = re.sub(re.compile(map[0]), map[1], self.str)
        return self.str
