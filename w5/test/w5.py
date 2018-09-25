import os, sys, re, traceback

root = os.path.abspath(os.path.join(os.getcwd().split('test')[0], 'src'))

input_path = os.path.abspath(os.path.join(os.getcwd().split('test')[0], 'input'))

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


# @O.k
# def dom_test_one():
#     """
#     Testing domination functions on weatherLong.csv.
#
#     The rows are first sorted by their 'dom' column,
#     then the 'humid' column is checked for monotonic nondecrease.
#     """
#
#     # Read in the data and calculate dom scores
#     data = Data()
#     data.rows(input_path + '/weatherLong.csv')
#     data.doms(1000)
#
#     # Sort the data by dom score
#     dom_sort = sorted(data.data_rows, key=lambda x: x[len(x) - 1], reverse=True)
#
#     # Ensure that 'humid' column is monotonically nondecreasing
#     for i in range(1, len(dom_sort)):
#         assert dom_sort[i - 1][2] <= dom_sort[i][2]
#
#     # Print the table
#
#     print()
#     for i in range(79):
#         print('-', end='')
#     print()
#
#     for name in data.names:
#         print('|', str.center(data.names[name], 10), end=' ')
#
#     print('|')
#     for i in range(79):
#         print('-', end='')
#     print()
#
#     for row in dom_sort:
#         for index, value in enumerate(row):
#             if data.names[index] == '>dom':
#                 print('|', str.center(str(round(value, 2)), 10), end=' ')
#             else:
#                 print('|', str.center(str(value), 10), end=' ')
#         print('|')
#
#     for i in range(79):
#         print('-', end='')
#     print('\n')
#
# @O.k
# def dom_test_two():
#     """
#     Testing domination functions on auto.csv.
#
#     The rows are first sorted by their 'dom' column,
#     then all columns we are maximizing or minimizing
#     in the top and bottom ten results are compared.
#     """
#
#     # Read in the data and calculate dom scores
#     data = Data()
#     data.rows(input_path + '/auto.csv')
#     data.doms(100)
#
#     # Sort the data by dom score
#     dom_sort = sorted(data.data_rows, key=lambda x: x[len(x) - 1], reverse=True)
#
#     dom_maxs = {'<weight': [], '>acceltn': [], '>mpg': []}
#     dom_mins = {'<weight': [], '>acceltn': [], '>mpg': []}
#
#     # Print the table top and bottom ten and store values to dom_maxs and dom_mins
#
#     print()
#     for i in range(115):
#         print('-', end='')
#     print()
#
#     for name in data.names:
#         print('|', str.center(data.names[name], len(data.names[name]) + 2), end=' ')
#
#     print('|')
#     for i in range(115):
#         print('-', end='')
#     print()
#
#     for i in range(10):
#         for index, value in enumerate(dom_sort[i]):
#             if data.names[index] == '<weight':
#                 dom_maxs['<weight'].append(value)
#             elif data.names[index] == '>acceltn':
#                 dom_maxs['>acceltn'].append(value)
#             elif data.names[index] == '>mpg':
#                 dom_maxs['>mpg'].append(value)
#             if data.names[index] == '>dom':
#                 print('|', str.center(str(round(value, 2)), len(data.names[index]) + 2), end=' ')
#             else:
#                 print('|', str.center(str(value), len(data.names[index]) + 2), end=' ')
#         print('|')
#
#     for i in range(57):
#         print('\/', end='')
#     print('\\\n')
#
#     for i in range(57):
#         print('\/', end='')
#     print('\\')
#
#     for i in range(len(dom_sort) - 10, len(dom_sort)):
#         for index, value in enumerate(dom_sort[i]):
#             if data.names[index] == '<weight':
#                 dom_mins['<weight'].append(value)
#             elif data.names[index] == '>acceltn':
#                 dom_mins['>acceltn'].append(value)
#             elif data.names[index] == '>mpg':
#                 dom_mins['>mpg'].append(value)
#             if data.names[index] == '>dom':
#                 print('|', str.center(str(round(value, 2)), len(data.names[index]) + 2), end=' ')
#             else:
#                 print('|', str.center(str(value), len(data.names[index]) + 2), end=' ')
#         print('|')
#
#     for i in range(115):
#         print('-', end='')
#     print('\n')
#
#     # Ensure that the columns we are maximizing and minimizing appear properly in the top and bottom ten
#     for i in range(10):
#         for j in range(10):
#             assert dom_maxs['<weight'][i] < dom_mins['<weight'][j]
#             assert dom_maxs['>acceltn'][i] > dom_mins['>acceltn'][j]
#             assert dom_maxs['>mpg'][i] > dom_mins['>mpg'][j]


@O.k
def disc_test():
    """
    Testing discretization functions on weatherLong.csv
    """

    data = Data()
    data.rows(input_path + '/weatherLong.csv')
    result = data.unsuper()

    for row in result:
        print(row)


if __name__ == "__main__":
    O.report()
