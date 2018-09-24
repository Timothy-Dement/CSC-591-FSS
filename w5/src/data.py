import math, os, random, re, sys

from num import Num
from sym import Sym

root = os.path.abspath(os.path.join(os.getcwd().split('src')[0], 'src'))

if root not in sys.path:
    sys.path.append(str(root))


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

        with open(file):

            for index, line in enumerate(open(file)):

                line = re.sub(r'[ \n\r\t]*|#.*', '', line).split(',')

                if index == 0:
                    self.header(line)
                else:
                    self.row(line)

    def doms(self, num_rand_rows=100):

        max_col = -math.inf

        for col in self.names:
            if col > max_col:
                max_col = col

        self.names[max_col + 1] = '>dom'

        for current_row in self.data_rows:

            current_row.append(0)

            for i in range(num_rand_rows):
                other_row = self.another(current_row)
                if self.dom(current_row, other_row):
                    current_row[len(current_row) - 1] += 1 / num_rand_rows

    def dom(self, current_row, other_row):

        current_shout = 0
        other_shout = 0

        for col_weight in self.weights:
            current_val = current_row[col_weight]
            other_val = other_row[col_weight]

            current_norm = self.nums[col_weight].num_norm(current_val)
            other_norm = self.nums[col_weight].num_norm(other_val)

            current_shout -= 10 ** (self.weights[col_weight] * (current_norm - other_norm) / len(self.weights))
            other_shout -= 10 ** (self.weights[col_weight] * (other_norm - current_norm) / len(self.weights))

        return current_shout < other_shout

    def another(self, current_row):

        other_row = random.randrange(len(self.data_rows))

        if current_row == other_row:
            self.another(current_row)
        else:
            return self.data_rows[other_row]
