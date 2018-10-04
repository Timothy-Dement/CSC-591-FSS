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


@O.k
def super_dom_one():
    """
    INCOMPLETE
    """

    data = Data()
    data.rows(input_path + '/weatherLong.csv')
    data.doms()
    data.super()

    print()
    table = PrettyTable(title='weatherLong.csv')
    table.field_names = list(data.names.values())

    for row in data.data_rows:
        round_row = row[:-1]
        round_row.append(round(row[len(row)-1], 2))
        table.add_row(round_row)

    print(table)
    print()

    ########
    #
    #  SOMEHOW NEED TO FIND SPLIT, THEN ASSERT
    #
    ########

if __name__ == "__main__":
    O.report()

@O.k
def super_dom_two():
    """
    INCOMPLETE
    """

    data = Data()
    data.rows(input_path + '/auto.csv')
    data.doms()
    data.super()

    print()

    ########
    #
    #  SOMEHOW NEED TO FIND SPLIT, THEN ASSERT
    #
    ########