import math
import os
import re
import sys
import traceback

from prettytable import PrettyTable

src_path = os.path.abspath(os.path.join(os.getcwd().split('test')[0], 'src'))

input_path = os.path.abspath(os.path.join(os.getcwd().split('test')[0], 'input'))

if src_path not in sys.path: sys.path.append(str(src_path))

from data import Data

class O:
    y = n = 0

    @staticmethod
    def report():
        print("\n# pass= %s fail= %s %%pass = %s%%" % (
            O.y, O.n, int(round(O.y * 100 / (O.y + O.n + 0.001)))))

    @staticmethod
    def k(f):
        try:
            print("\n-----| %s |-----------------------" % f.__name__)
            if f.__doc__:
                print("# " + re.sub(r'\n[ \t]*', "\n# ", f.__doc__))
            f()
            print("# pass")
            O.y += 1
        except:
            O.n += 1
            print(traceback.format_exc())
        return f

def close(x, y, c=0.01):
    return math.fabs((x - y) / y) < c

@O.k
def super_dom_one():
    """
    Testing supervised domination on weatherLong.csv ...

    1. Calculate dom scores for weatherLong.csv rows
    2. Perform supervised discretizaion (goal: dom)
    3. Find the attribute to split that minimizes expected value
    4. Check that the attribute and expected value are relatively stable
    """

    data = Data()
    data.rows(input_path + '/weatherLong.csv')
    data.doms()
    data.super()

    splitter, xpect = data.splitter()

    print(f'\nSplit:\t{data.names[splitter]}')
    print(f'Xpect:\t{round(xpect, 4)}')

    assert '$temp' == data.names[splitter]
    assert close(xpect, 0.16, 0.5)

    print()
    table = PrettyTable(title='weatherLong.csv')
    table.field_names = list(data.names.values())

    for row in data.data_rows:
        round_row = row[:-1]
        round_row.append(round(row[len(row)-1], 2))
        table.add_row(round_row)

    print(table)
    print()

if __name__ == "__main__":
    O.report()

@O.k
def super_dom_two():
    """
    Testing supervised domination on auto.csv ...

    1. Calculate dom scores for auto.csv rows
    2. Perform supervised discretizaion (goal: dom)
    3. Find the attribute to split that minimizes expected value
    4. Check that the attribute and expected value are relatively stable
    """

    data = Data()
    data.rows(input_path + '/auto.csv')
    data.doms()
    data.super()

    splitter, xpect = data.splitter()

    print(f'\nSplit:\t{data.names[splitter]}')
    print(f'Xpect:\t{round(xpect, 4)}')

    print()

    assert '$horsepower' == data.names[splitter]
    assert close(xpect, 0.09, 0.5)
