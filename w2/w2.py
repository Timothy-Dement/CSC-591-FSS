import re, traceback


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


DATA1 = """
outlook,$temp,?humidity,windy,play
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,100,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no"""

DATA2 = """
    outlook,   # weather forecast.
    $temp,     # degrees farenheit
    ?humidity, # relative humidity
    windy,     # wind is high
    play       # yes,no
    sunny,85,85,FALSE,no
    sunny,80,90,TRUE,no
    overcast,83,86,FALSE,yes

    rainy,70,96,FALSE,yes
    rainy,68,80,FALSE,yes
    rainy,65,70,TRUE,no
    overcast,64,

                  65,TRUE,yes
    sunny,72,95,FALSE,no
    sunny,69,70,FALSE,yes
    rainy,75,80,FALSE,yes
          sunny,
                75,70,TRUE,yes
    overcast,100,90,TRUE,yes
    overcast,81,75,FALSE,yes # unique day
    rainy,71,91,TRUE,no"""


########
#
#  Functions beginning with my_ were my first attempts before Dr. Menzies posted his solutions.
#  Functions not beginning with my_ added in logic from the posted solutions.
#
########

def my_lines(s):
    """"
    Return contents, one line at a time.
    """
    return s.splitlines()


def my_rows(src):
    """
    Kill bad characters. If line ends in ',' then join to next. Skip blank lines.
    """

    stripped_rows = list()

    for index, row in enumerate(src):
        if row:
            stripped_rows.append(row.split('#')[0].replace(' ', ''))
            while stripped_rows[-1].endswith(','):
                stripped_rows[-1] = stripped_rows[-1] + src[index + 1].split('#')[0].replace(' ', '')
                del src[index + 1]

    return stripped_rows


def my_cols(src):
    """
    If a column name on row1 contains '?' then skip over that column.
    """

    invalid_cols = set()

    for index, col in enumerate(src[0].split(',')):
        if '?' in col:
            invalid_cols.add(index)

    split_rows = list()

    for row in src:
        split_row = row.split(',')
        valid_row = list()
        for index, col in enumerate(split_row):
            if index not in invalid_cols:
                valid_row.append(col)
        split_rows.append(valid_row)

    return split_rows


def my_prep(src):
    """
    If a column name on row1 contains '$' coerce strings in that column to a float.
    """

    typed_rows = list()
    legend = src[0]

    for o_index, row in enumerate(src):
        typed_row = list()
        for i_index, col in enumerate(row):
            if o_index != 0 and '$' in legend[i_index]:
                typed_row.append(float(col))
            else:
                typed_row.append(col)
        typed_rows.append(typed_row)

    return typed_rows


def ok0(s):
    correct = [['outlook', '$temp', 'windy', 'play'],
               ['sunny', 85.0, 'FALSE', 'no'],
               ['sunny', 80.0, 'TRUE', 'no'],
               ['overcast', 83.0, 'FALSE', 'yes'],
               ['rainy', 70.0, 'FALSE', 'yes'],
               ['rainy', 68.0, 'FALSE', 'yes'],
               ['rainy', 65.0, 'TRUE', 'no'],
               ['overcast', 64.0, 'TRUE', 'yes'],
               ['sunny', 72.0, 'FALSE', 'no'],
               ['sunny', 69.0, 'FALSE', 'yes'],
               ['rainy', 75.0, 'FALSE', 'yes'],
               ['sunny', 75.0, 'TRUE', 'yes'],
               ['overcast', 100.0, 'TRUE', 'yes'],
               ['overcast', 81.0, 'FALSE', 'yes'],
               ['rainy', 71.0, 'TRUE', 'no']]

    for index, row in enumerate(my_prep(my_cols(my_rows(my_lines(s))))):
        print(row)
        assert row == correct[index]


def lines(s):
    """"
    Return contents, one line at a time.
    """

    for line in s.splitlines(): yield line


def rows(src):
    """
    Kill bad characters. If line ends in ',' then join to next. Skip blank lines.
    """

    cache = []  # Will be used to collect 'partial' lines

    for line in src:

        line = re.sub(r'[ \n\r\t]|#.*', '', line)  # Remove 'blank' chars and all '#' and anything after

        if line:  # Only consider non-blank lines

            cache += [line]  # Add the line to the end of the cache

            if not line.endswith(','):  # If the line does not end with ',' ...

                line = ''.join(cache)  # ... then we are returning the cache contents

                cache = []  # ... reset the cache

                yield line  # ... and yield the line


def cols(src):
    """
    If a column name on row1 contains '?' then skip over that column.
    """

    invalid_cols = set()

    headers = []

    for index, row in enumerate(src):

        if index == 0:

            headers = row.split(',')

            for index, col in enumerate(headers):

                if '?' in col: invalid_cols.add(index)

        row_builder = []

        row = row.split(',')

        for index, col in enumerate(row):

            if index not in invalid_cols: row_builder.append(col)

        yield row_builder


def prep(src):
    """
    If a column name on row1 contains '$' coerce strings in that column to a float.
    """

    num_cols = set()

    for row_index, row in enumerate(src):

        if row_index == 0:

            for col_index, col in enumerate(row):

                if '$' in col: num_cols.add(col_index)

            yield row

        else:

            for num_col in num_cols:

                row[num_col] = float(row[num_col])

            yield row


def ok0(s):
    correct = [['outlook', '$temp', 'windy', 'play'],
               ['sunny', 85.0, 'FALSE', 'no'],
               ['sunny', 80.0, 'TRUE', 'no'],
               ['overcast', 83.0, 'FALSE', 'yes'],
               ['rainy', 70.0, 'FALSE', 'yes'],
               ['rainy', 68.0, 'FALSE', 'yes'],
               ['rainy', 65.0, 'TRUE', 'no'],
               ['overcast', 64.0, 'TRUE', 'yes'],
               ['sunny', 72.0, 'FALSE', 'no'],
               ['sunny', 69.0, 'FALSE', 'yes'],
               ['rainy', 75.0, 'FALSE', 'yes'],
               ['sunny', 75.0, 'TRUE', 'yes'],
               ['overcast', 100.0, 'TRUE', 'yes'],
               ['overcast', 81.0, 'FALSE', 'yes'],
               ['rainy', 71.0, 'TRUE', 'no']]

    print()

    for index, row in enumerate(my_prep(my_cols(my_rows(my_lines(s))))):
        print(row)
        assert row == correct[index]

    print()

@O.k
def ok1():
    """
    Testing original implementation on standard data.
    """
    ok0(DATA1)


@O.k
def ok2():
    """
    Testing original implementation on nonstandard data.
    """
    ok0(DATA2)


def ok3(s):
    correct = [['outlook', '$temp', 'windy', 'play'],
               ['sunny', 85.0, 'FALSE', 'no'],
               ['sunny', 80.0, 'TRUE', 'no'],
               ['overcast', 83.0, 'FALSE', 'yes'],
               ['rainy', 70.0, 'FALSE', 'yes'],
               ['rainy', 68.0, 'FALSE', 'yes'],
               ['rainy', 65.0, 'TRUE', 'no'],
               ['overcast', 64.0, 'TRUE', 'yes'],
               ['sunny', 72.0, 'FALSE', 'no'],
               ['sunny', 69.0, 'FALSE', 'yes'],
               ['rainy', 75.0, 'FALSE', 'yes'],
               ['sunny', 75.0, 'TRUE', 'yes'],
               ['overcast', 100.0, 'TRUE', 'yes'],
               ['overcast', 81.0, 'FALSE', 'yes'],
               ['rainy', 71.0, 'TRUE', 'no']]

    print()

    for index, row in enumerate(prep(cols(rows(lines(s))))):
        print(row)
        assert row == correct[index]

    print()

@O.k
def ok4():
    """
    Testing second implementation on standard data.
    """
    ok3(DATA1)

@O.k
def ok5():
    """
    Testing second implementationon nonstandard data.
    """
    ok3(DATA2)

if __name__ == "__main__":
    O.report()
