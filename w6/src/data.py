import collections, math, os, random, re, sys

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
        self.splits = collections.defaultdict(list)

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

    def super(self):

        goal = len(self.valid_cols)
        enough = len(self.data_rows) ** 0.5

        def band(col, lo, hi):

            if lo == 0:
                return '..' + str(self.data_rows[hi][col])
            elif  hi == most:
                return str(self.data_rows[lo][col]) + '..'
            else:
                return str(self.data_rows[lo][col]) + '..' + str(self.data_rows[hi][col])

        def argmin(col, lo, hi):

            cut = None

            xl, xr = Num(), Num()
            yl, yr = Num(), Num()

            for i in range(lo, hi + 1):
                xr.num_inc(self.data_rows[i][col])
                yr.num_inc(self.data_rows[i][goal])

            bestx = xr.standard_deviation
            besty = yr.standard_deviation

            mu = yr.mean

            if (hi - lo) > 2 * enough:

                for i in range(lo, hi + 1):

                    x = self.data_rows[i][col]
                    y = self.data_rows[i][goal]

                    xr.num_dec(x)
                    xl.num_inc(x)

                    yr.num_dec(y)
                    yl.num_inc(y)

                    if xl.count >= enough and xr.count >= enough:

                        tmpx = xl.num_xpect(xr) * 1.05
                        tmpy = yl.num_xpect(yr) * 1.05

                        if tmpx < bestx and tmpy < besty:
                            cut, bestx, besty = i, tmpx, tmpy

            return cut, mu, besty

        def cuts(col, lo, hi, pre):

            txt = pre + str(self.data_rows[lo][col]) + '..' + str(self.data_rows[hi][col])

            cut, mu, sd = argmin(col, lo, hi)

            if cut:

                sys.stderr.write(txt + '\n')
                cuts(col, lo, cut, pre + '|..')
                cuts(col, cut + 1, hi, pre + '|..')

            else:

                s = band(col, lo, hi)
                sys.stderr.write(txt + ' : mu = ' + str(math.floor(100 * mu)) + ' | sd = ' + str(round(sd, 2)) + '\n')

                metrics = { 'mu': math.floor(100 * mu), 'sd': sd }

                self.splits[indep].append(metrics)

                for i in range(lo, hi + 1):
                    self.data_rows[i][col] = s

        def stop(col):

            bottom = len(self.data_rows) - 1

            while self.data_rows[bottom][col] == '?':
                bottom -= 1

            return bottom

        for indep in self.indeps:

            if indep in self.nums:
                self.data_rows.sort(key=lambda x: math.inf if x[indep] == '?' else x[indep])

                most = stop(indep)

                sys.stderr.write('\n-- ' + self.names[indep] + ' : ' + str(most) + ' ----------\n')

                cuts(indep, 0, most, '|..')


    def splitter(self):

        best_splitter, best_xpect = None, math.inf

        for indep in self.splits:

            total = 0
            xpect = 0

            for split in self.splits[indep]:
                total += split['mu']

            for split in self.splits[indep]:
                xpect += split['mu'] / total * split['sd']

            if xpect < best_xpect:
                best_splitter = indep
                best_xpect = xpect

        return best_splitter, best_xpect