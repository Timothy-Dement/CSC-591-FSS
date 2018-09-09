import math, random, re, traceback

from sample import Sample

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
    return math.fabs((x - y) / x) < c

@O.k
def sample_test():
    """
    Testing sample.py
    """

    samples = []

    for i in range(5, 11):

        samples.append(Sample(2**i))

    for i in range(10000):

        random_number = random.random()

        for sample in samples:

            sample.sample_inc(random_number)

    print()

    for sample in samples:

        print(sample.maximum_size, sample.nth(0.5))

        assert close(sample.nth(0.5), 0.5, 0.2)

    print()

if __name__== "__main__":
  O.report()
