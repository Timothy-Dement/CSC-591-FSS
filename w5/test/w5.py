import os, sys, re, traceback

root = os.path.abspath(os.path.join(os.getcwd().split('src')[0], 'src'))

if root not in sys.path:
    sys.path.append(str(root))

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
def dom_test_one():
    """
    Testing domination functions on weatherLong.csv
    """

    data = Data()
    data.rows('../input/weatherLong.csv')
    data.doms()

    dom_sort = sorted(data.data_rows, key=lambda x: x[len(x) - 1], reverse=True)




@O.k
def dom_test_two():
    """
    Testing domination functions on auto.csv
    """

if __name__ == "__main__":
    O.report()
