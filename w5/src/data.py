import math, os, random, re, sys

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

    def unsuper(self):

        enough = len(self.data_rows) ** 0.5

        sorted_rows = []

        for indep in self.indeps:
            if indep in self.nums:
                sorted_rows = sorted(self.data_rows, key=lambda x: math.inf if x[indep] == '?' else x[indep])

        stop = len(sorted_rows) - 1

        for indep in self.indeps:
            if indep in self.nums:
                while sorted_rows[stop][indep] == '?':
                    stop -= 1

        def band(col, lo, hi):

            if lo == 0:
                return '..' + str(sorted_rows[hi][col])
            elif hi == stop:
                return str(sorted_rows[lo][col]) + '..'
            else:
                return str(sorted_rows[lo][col]) + '..' + str(sorted_rows[hi][col])

        def argmin(col, lo, hi):

            cut = None

            if hi - lo > 2 * enough:

                l, r = Num(), Num()

                for i in range(lo, hi + 1):
                    r.num_inc(sorted_rows[i][col])

                best = r.standard_deviation

                for i in range(lo, hi + 1):

                    curr_val = sorted_rows[i][col]

                    l.num_inc(curr_val)
                    r.num_dec(curr_val)

                    if l.count >= enough and r.count >= enough:

                        tmp = l.num_xpect(r) * 1.05

                        if tmp < best:
                            cut, best = i, tmp

            return cut

        def cuts(col, lo, hi, pre):

            txt = pre + str(sorted_rows[lo][col]) + '..' + str(sorted_rows[hi][col])

            cut = argmin(col, lo, hi)

            if cut:

                sys.stderr.write(txt + '\n')
                cuts(col, lo, cut, pre + '|..')
                cuts(col, cut + 1, hi, pre + '|..')

            else:

                b = band(col, lo, hi)
                sys.stderr.write(txt + ' (' + b + ')\n')

                for i in range(lo, hi + 1):
                    sorted_rows[i][col] = b

        for indep in self.indeps:
            if indep in self.nums:
                sys.stderr.write('\n-- ' + self.names[indep] + ' : ' + str(stop) + ' ----------\n')
                cuts(indep, 0, stop, '|..')

        return sorted_rows
