import math, re, traceback

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
def weather_test():
    """
    Testing weather.csv file input
    """

    data = Data()
    data.rows('weather.csv')
    data.print_table()

    for sym in data.syms:

        if data.names[sym] == 'outlook':

            assert data.syms[sym].count == 14
            assert data.syms[sym].mode == 'sunny'
            assert data.syms[sym].sym_dict[data.syms[sym].mode] == 5

        elif data.names[sym] == 'wind':

            assert data.syms[sym].count == 14
            assert data.syms[sym].mode == 'FALSE'
            assert data.syms[sym].sym_dict[data.syms[sym].mode] == 8

        elif data.names[sym] == '!play':

            assert data.syms[sym].count == 14
            assert data.syms[sym].mode == 'yes'
            assert data.syms[sym].sym_dict[data.syms[sym].mode] == 9

    for num in data.nums:

        if data.names[num] == '$temp':

            assert data.nums[num].count == 14
            assert close(data.nums[num].mean, 73.57)
            assert close(data.nums[num].standard_deviation, 6.57)

@O.k
def weather_long_test():
    """
    Testing weatherLong.csv file input
    """

    data = Data()
    data.rows('weatherLong.csv')
    data.print_table()

    for sym in data.syms:

        if data.names[sym] == '%outlook':

            assert data.syms[sym].count == 28
            assert data.syms[sym].mode == 'sunny'
            assert data.syms[sym].sym_dict[data.syms[sym].mode] == 10

        elif data.names[sym] == 'wind':

            assert data.syms[sym].count == 28
            assert data.syms[sym].mode == 'FALSE'
            assert data.syms[sym].sym_dict[data.syms[sym].mode] == 16

        elif data.names[sym] == '!play':

            assert data.syms[sym].count == 28
            assert data.syms[sym].mode == 'yes'
            assert data.syms[sym].sym_dict[data.syms[sym].mode] == 18

    for num in data.nums:

        if data.names[num] == '$temp':
            assert data.nums[num].count == 28
            assert close(data.nums[num].mean, 73.57)
            assert close(data.nums[num].standard_deviation, 6.45)

        elif data.names[num] == '<humid':
            assert data.nums[num].count == 28
            assert close(data.nums[num].mean, 81.64)
            assert close(data.nums[num].standard_deviation, 10.09)

@O.k
def auto_test():
    """
    Testing auto.csv file input
    """

    data = Data()
    data.rows('auto.csv')
    data.print_table()

    for sym in data.syms:

        if data.names[sym] == '%cylinders':

            assert data.syms[sym].count == 398
            assert data.syms[sym].mode == '4'
            assert data.syms[sym].sym_dict[data.syms[sym].mode] == 204

        elif data.names[sym] == 'origin':

            assert data.syms[sym].count == 398
            assert data.syms[sym].mode == '1'
            assert data.syms[sym].sym_dict[data.syms[sym].mode] == 249

    for num in data.nums:

        if data.names[num] == '$displacement':

            assert data.nums[num].count == 398
            assert close(data.nums[num].mean, 193.43)
            assert close(data.nums[num].standard_deviation, 104.27)

        elif data.names[num] == '$horsepower':

            assert data.nums[num].count == 392
            assert close(data.nums[num].mean, 104.47)
            assert close(data.nums[num].standard_deviation, 38.49)

        elif data.names[num] == '<weight':

            assert data.nums[num].count == 398
            assert close(data.nums[num].mean, 2970.42)
            assert close(data.nums[num].standard_deviation, 846.84)

        elif data.names[num] == '>acceltn':

            assert data.nums[num].count == 398
            assert close(data.nums[num].mean, 15.57)
            assert close(data.nums[num].standard_deviation, 2.76)

        elif data.names[num] == '$model':

            assert data.nums[num].count == 398
            assert close(data.nums[num].mean, 76.01)
            assert close(data.nums[num].standard_deviation, 3.70)

        elif data.names[num] == '>mpg':

            assert data.nums[num].count == 398
            assert close(data.nums[num].mean, 23.84)
            assert close(data.nums[num].standard_deviation, 8.34)

if __name__ == "__main__":
    O.report()
