import re

from num import Num
from sym import Sym


class Data:

    def __init__(self):
        self.weights = {}
        self.syms = {}
        self.nums = {}
        self.indeps = []
        self.class_col = None
        self.data_rows = []
        self.names = {}
        self.valid_cols = []

    def independent(self, col):
        return col not in self.weights and self.class_col != col

    def dependent(self, col):
        return not self.independent(col)

    def header(self, cells):

        for index, cell in enumerate(cells):

            if '?' not in cell:

                self.valid_cols.append(index)
                self.names[index] = cell

                if re.match('[<>$]', cell):
                    self.nums[index] = Num()
                else:
                    self.syms[index] = Sym()

                if re.match('<', cell):
                    self.weights[index] = -1
                elif re.match('>', cell):
                    self.weights[index] = 1
                elif re.match('!', cell):
                    self.class_col = index
                else:
                    self.indeps.append(index)

    def row(self, cells):

        self.data_rows.append([])
        row = len(self.data_rows) - 1

        for valid_col in self.valid_cols:

            content = cells[valid_col]

            if '?' not in content:

                if valid_col in self.nums:
                    content = float(content)
                    self.nums[valid_col].num_inc(content)
                else:
                    self.syms[valid_col].sym_inc(content)

            self.data_rows[row].append(content)

    def rows(self, file):

        for index, line in enumerate(open(file)):

            line = re.sub(r'[ \n\r\t]*|#.*', '', line).split(',')

            if index == 0:
                self.header(line)
            else:
                self.row(line)

    def print_table(self):

        print()

        print('------------------------------------------------')
        print('| ', str.center('NAME', 13),
              ' | ', str.center('COUNT', 5),
              ' | ',str.center('MODE', 5),
              ' | ', str.center('FREQ', 4),
              ' |')
        print('------------------------------------------------')
        for sym in self.syms:
            print('| ', str.ljust(self.names[sym], 13),
                  ' | ', str.rjust(str(self.syms[sym].count), 5),
                  ' | ', str.ljust(self.syms[sym].mode, 5),
                  ' | ', str.rjust(str(self.syms[sym].sym_dict[self.syms[sym].mode]), 4),
                  ' |')
        print('------------------------------------------------')

        print()

        print('----------------------------------------------------')
        print('| ', str.center('NAME', 13),
              ' | ', str.center('COUNT', 5),
              ' | ', str.center('MEAN', 7),
              ' | ', str.center('STDV', 6),
              ' |')
        print('----------------------------------------------------')
        for num in self.nums:
            print('| ', str.ljust(self.names[num], 13),
                  ' | ', str.rjust(str(self.nums[num].count), 5),
                  ' | ', str.rjust(str(round(self.nums[num].mean, 2)), 7),
                  ' | ', str.rjust(str(round(self.nums[num].standard_deviation, 2)), 6),
                  ' |')
        print('----------------------------------------------------')

        print()