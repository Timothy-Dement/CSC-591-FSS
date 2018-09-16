from math import log2


class Sym:

    def __init__(self):

        self.sym_dict = {}
        self.mode = None
        self.count = 0
        self.entropy = None

    def sym_inc(self, new):

        self.entropy = None

        self.count += 1

        if new in self.sym_dict:
            self.sym_dict[new] += 1

        else:
            self.sym_dict[new] = 1

        if not self.mode:
            self.mode = new

        elif self.sym_dict[self.mode] < self.sym_dict[new]:
            self.mode = new

    def syms(self, sym_list):

        for sym in sym_list:
            self.sym_inc(sym)

    def sym_dec(self, remove):

        self.entropy = None

        self.count -= 1

        if self.sym_dict[remove] == 1:
            del self.sym_dict[remove]

        else:
            self.sym_dict[remove] -= 1

    def sym_ent(self):

        if not self.entropy:

            self.entropy = 0

            for sym in self.sym_dict:
                probability = self.sym_dict[sym] / self.count

                self.entropy -= probability * log2(probability)

        return self.entropy
