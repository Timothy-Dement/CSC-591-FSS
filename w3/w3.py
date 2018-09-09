import math, random, re, traceback

from sample import Sample
from num import Num
from sym import Sym


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
def sample_test():
    """
    Testing sample.py ...
    """

    samples = []

    for i in range(5, 11):
        samples.append(Sample(2 ** i))

    for i in range(10 ** 4):

        random_number = random.random()

        for sample in samples:
            sample.sample_inc(random_number)

    print()

    for sample in samples:
        print(sample.maximum_size, ':', sample.nth(0.5))

        assert close(sample.nth(0.5), 0.5, 0.2)

    print()


@O.k
def num_test():
    """
    Testing num.py ...
    """

    num = Num(30)

    num_list = [4, 10, 15, 38, 54,
                57, 62, 83, 100, 100,
                174, 190, 215, 225, 233,
                250, 260, 270, 299, 300,
                306, 333, 350, 375, 443,
                475, 525, 583, 780, 1000]

    num.nums(num_list)

    print()

    print('MU', ':', num.mean)
    print('SD', ':', num.standard_deviation)

    assert close(num.mean, 270.3)
    assert close(num.standard_deviation, 231.946)

    print()


@O.k
def sym_test():
    """
    Testing sym.py ...
    """

    sym = Sym()

    sym_list = ['y', 'y', 'y', 'y', 'y', 'y', 'y',
                'y', 'y', 'n', 'n', 'n', 'n', 'n']

    sym.syms(sym_list)

    print()
    print('ENT', ':', sym.sym_ent())
    print()

    assert(close(sym.sym_ent(), 0.9403))


if __name__ == "__main__":
    O.report()
