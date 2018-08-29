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


########
#
#  1. Page 5: Whitespace Formatting
#
########

@O.k
def p5_whitespace_formatting():
    """
    - Code blocks are delimited with indentation
    - Whitespace is ignored within parentheses and brackets
    - A backslash can be used if a statement spans multiple lines
    """

    # Code blocks are delimited with indentation

    inner_counter = 0
    outer_counter = 0

    for i in [1, 2, 3, 4, 5, 6, 7]:
        outer_counter += 1
        for j in [1, 2, 3, 4, 5, 6]:
            inner_counter += 1

    assert inner_counter == 42
    assert outer_counter == 7

    # Whitespace is ignored within parentheses and brackets

    single_line_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    multi_line_list = [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]]

    assert single_line_list == multi_line_list

    # A backslash can be used if a statement spans multiple lines

    single_line_sum = 6 + 7
    multi_line_sum = 6 + \
                     7

    assert single_line_sum == multi_line_sum


########
#
#  2. Page 6: Modules
#
########

@O.k
def p6_modules():
    """
    - Modules are loaded with the import statement
    - Modules can be loaded under a given alias
    - Import statements may overshadow existing variables
    """

    # Modules are loaded with the import statement

    import re
    result_one = re.match("[0-9]+", "42")
    assert result_one is not None

    # Modules can be loaded under a given alias

    import re as regex
    result_two = regex.match("[0-9]+", "42")
    assert result_two is not None

    # Import statements may overshadow existing variables

    match = 10
    assert match is 10

    from re import match
    assert match is not 10


########
#
#  3. Page 7: Arithmetic
#
########

@O.k
def p7_arithmetic():
    """
    - A single forward slash is used for normal division
    - Two forward slashes are used for integer division
    """

    # A single forward slash is used for normal division

    quotient_one = 5 / 2
    assert quotient_one == 2.5
    assert type(quotient_one) == float

    # Two forward slashes are used for integer division

    quotient_two = 5 // 2
    assert quotient_two == 2
    assert type(quotient_two) == int


########
#
#  4. Page 8: Functions
#
########

@O.k
def p8_functions():
    """
    - Functions take zero or more inputs and return a corresponding output
    - Functions can be assigned to variables and passed to other functions
    - Anonymous functions can be created using the lambda keyword
    - Function parameters can be given default arguments
    - Arguments can be specified by name
    """

    # Functions take zero or more inputs and return a corresponding output

    def double(x):
        return x * 2

    assert double(21) == 42

    # Functions can be assigned to variables and passed to other functions

    def apply_to_one(f):
        return f(1)

    assigned_double = double
    assert apply_to_one(assigned_double) == 2

    # Anonymous functions can be created using the lambda keyword

    double_lambda = apply_to_one(lambda x: double(x) + 40)
    assert double_lambda == 42

    # Function parameters can be given default arguments

    def subtract(a=0, b=0):
        return a - b

    assert subtract() == 0

    # Arguments can be specified by name

    assert subtract(10, 5) == 5
    assert subtract(a=10) == 10
    assert subtract(b=5) == -5


########
#
#  5. Page 9: Strings
#
########

@O.k
def p9_strings():
    """
    - Strings can be delimited with single- or double-quotation marks
    - Use a backslash to encode special characters
    - Raw strings are created using r""
    - Multi-line strings are created using triple double-quotation marks
    """

    # Strings can be delimited with single- or double-quotation marks

    single_quoted_string = 'Hello, World!'
    double_quoted_string = "Hello, World!"
    assert single_quoted_string == double_quoted_string

    # Use a backslash to encode special characters

    tab_string = "\t"
    assert len(tab_string) == 1

    # Raw strings are created using r""

    not_tab_string = r"\t"
    assert len(not_tab_string) == 2

    # Multi-line strings are created using triple double-quotation marks

    multi_line_string_one = """Line 1
    Line 2
    Line 3"""

    multi_line_string_two = "Line 1\n    Line 2\n    Line 3"

    assert multi_line_string_one == multi_line_string_two


########
#
#  6. Page 10: Exceptions
#
########

@O.k
def p10_exceptions():
    """
    - Exceptions are handled using try and except
    """

    # Exceptions ae handled using try and except

    def divide_ten_by(x):
        try:
            return 10 / x
        except ZeroDivisionError:
            return "Cannot divide by zero"

    assert divide_ten_by(5) == 2.0
    assert divide_ten_by(0) == "Cannot divide by zero"


########
#
#  7. Page 11-12: Lists
#
########

@O.k
def p11to12_lists():
    """
    - Lists are specified using enclosing brackets
    - A sequential numeric list can be created with range(n)
    - List elements are referenced with indices in square brackets
    - Lists can be sliced with square brackets and colons
    - The in operator checks if a list contains a given element
    - Lists are concatenated (destructively) with extend
    - Lists are concatenated (non-destructively) with list addition
    - An element can be added to a list using append
    - Lists can be unpacked by specifying a variable list in an assignment statement
    - An underscore is commonly used to reference unpacked elements that will not be used
    """

    # Lists are specified using enclosing brackets

    integer_list_one = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # A sequential numeric list can be created with range(n)

    integer_list_two = range(10)

    for x in range(10):
        assert integer_list_one[x] == integer_list_two[x]

    # List elements are referenced with indices in square brackets

    zero = integer_list_one[0]
    assert zero == 0

    nine = integer_list_one[-1]
    assert nine == 9

    integer_list_one[0] = 42
    assert integer_list_one[0] == 42

    # Lists can be sliced with square brackets and colons

    first_three = integer_list_one[:3]
    assert first_three == [42, 1, 2]

    seven_to_end = integer_list_one[7:]
    assert seven_to_end == [7, 8, 9]

    middle_two = integer_list_one[3:7]
    assert middle_two == [3, 4, 5, 6]

    last_three = integer_list_one[-3:]
    assert last_three == [7, 8, 9]

    # The in operator checks if a list contains a given element

    assert 42 in integer_list_one
    assert 0 not in integer_list_one

    # Lists are concatenated (destructively) with extend

    integer_list_three = [42, 1, 2, 3, 4, 5, 6]
    integer_list_three.extend([7, 8, 9])

    assert integer_list_three == integer_list_one

    # Lists are concatenated (non-destructively) with list addition

    integer_list_four = [42, 1, 2, 3, 4, 5, 6]
    integer_list_five = [7, 8, 9]
    integer_list_six = integer_list_four + integer_list_five

    assert integer_list_four != integer_list_one
    assert integer_list_six == integer_list_one

    # An element can be added to a list using append

    integer_list_five.append(10)
    assert integer_list_five == [7, 8, 9, 10]

    # Lists can be unpacked by specifying a variable list in an assignment statement

    seven, eight, nine, ten = integer_list_five
    assert seven == 7
    assert eight == 8
    assert nine == 9
    assert ten == 10

    # An underscore is commonly used to reference unpacked elements that will not be used

    the_answer, _, _, _, _, _, _ = integer_list_four
    assert the_answer == 42


########
#
#  8. Page 13: Tuples
#
########

@O.k
def p8_tuples():
    """
    - Tuples are specified using enclosing parentheses
    - As opposed to lists, tuples are immutable, i.e., they cannot be modified
    - Tuples can be used to return multiple values from a function
    - Tuples can be used for multiple assignment
    """

    # Tuples are specified by using enclosing parentheses

    list_one = [1, 2, 3]
    tuple_one = (1, 2, 3)

    assert list_one != tuple_one

    # As opposed to lists, tuples are immutable, i.e., they cannot be modified

    def set_first_element(collection):
        try:
            collection[0] = 42
        except TypeError:
            return "Cannot modify a tuple"

    set_first_element(list_one)
    assert list_one == [42, 2, 3]

    assert (set_first_element(tuple_one)) == "Cannot modify a tuple"
    assert tuple_one == (1, 2, 3)

    # Tuples can be used to return multiple values from a function

    def sum_and_product(x, y):
        return (x + y), (x * y)

    sp = sum_and_product(6, 7)

    assert sp == (13, 42)

    # Tuples can be used for multiple assignment

    s, p = sum_and_product(6, 7)

    assert s == 13
    assert p == 42


########
#
#  9. Page 14-16: Dictionaries
#
########

@O.k
def p14to16_dictionaries():
    """
    - Dictonaries are key-value pairs enclosed in curly braces
    - Empty dictionaries are created with empty curly braces or dict()
    - Dictionary elements are referenced by their keys in square brackets
    - Use in to check for the presence of a key in a dictionary
    - A standard or specified default value is returned when referencing a missing key
    - Key-value pairs are assigned using square brackets
    - Dictionaries have methods for returning all keys, all values, and all tuples
    - When you try to look up a key a defaultdict does not contain, it adds the key with the function you specify
    - Counters turn sequences of values into defaultdict(int)-like objects mapping keys to counts
    - Counters have a frequently-used most_common method
    """

    # Dictonaries are key-value pairs enclosed in curly braces

    dict_one = { "fname": "Timothy", "lname": "Dement" }
    dict_two = { "lname": "Dement", "fname": "Timothy" }

    assert dict_one == dict_two

    # Empty dictionaries are created with empty curly braces or dict()

    assert {} == dict()

    # Dictionary elements are referenced by their keys in square brackets

    assert dict_one["fname"] == "Timothy"

    # Use in to check for the presence of a key in a dictionary

    assert "fname" in dict_one
    assert "mname" not in dict_one

    # A standard (None) or specified default value is returned when getting a missing key

    assert dict_one.get("fname", "MISSING") == "Timothy"
    assert dict_one.get("mname", "MISSING") == "MISSING"
    assert dict_one.get("mname") is None

    # Key-value pairs are assigned using square brackets

    dict_one["mname"] = "Miller"
    assert dict_one == { "fname": "Timothy", "mname": "Miller", "lname": "Dement" }

    # Dictionaries have methods for returning all keys, all values, and all tuples

    assert list(dict_one.keys()) == ["fname", "lname", "mname"]
    assert list(dict_one.values()) == ["Timothy", "Dement", "Miller"]
    assert list(dict_one.items()) == [("fname", "Timothy"), ("lname", "Dement"), ("mname", "Miller")]

    # When you try to look up a key a defaultdict does not contain, it adds the key with the function you specify

    from collections import defaultdict

    phrase = "how much wood could a woodchuck chuck if a woodchuck could chuck wood"

    word_count = defaultdict(int)

    for word in phrase.split():
        word_count[word] += 1

    assert 1 == word_count["how"] \
           == word_count["much"] \
           == word_count["if"]

    assert 2 == word_count["wood"] \
           == word_count["could"] \
           == word_count["a"] \
           == word_count["woodchuck"] \
           == word_count["chuck"]

    # Counters turn sequences of values into defaultdict(int)-like objects mapping keys to counts

    from collections import Counter

    letter_count = Counter(phrase.replace(" ", ""))

    assert letter_count == {'o': 11,
                            'c': 11,
                            'u': 7,
                            'h': 6,
                            'd': 6,
                            'w': 5,
                            'k': 4,
                            'l': 2,
                            'a': 2,
                            'm': 1,
                            'i': 1,
                            'f': 1}

    # Counters have a frequently-used most_common method

    assert letter_count.most_common(3) == [('o', 11), ('c', 11), ('u', 7)]

########
#
#  10. Page 17: Sets
#
########

@O.k
def p17_sets():

    """
    - Sets represent collections of distinct elements
    - The in operation is much faster on sets than it is on lists
    - A set can be used to find distinct items in a collection
    """

    # Sets represent collections of distinct elements

    set_one = set()

    set_one.add(1)
    set_one.add(2)

    assert len(set_one) == 2

    set_one.add(2)

    assert len(set_one) == 2

    # The in operation is much faster on sets than it is on lists

    import time

    long_list = range(999999)
    long_set = set(long_list)

    list_start = time.perf_counter()
    1000000 in long_list
    list_end = time.perf_counter()

    list_time = list_end - list_start

    set_start = time.perf_counter()
    1000000 in long_set
    set_end = time.perf_counter()

    set_time = set_end - set_start

    assert set_time < list_time

    # A set can be used to find distinct items in a collection

    phrase = "how much wood could a woodchuck chuck if a woodchuck could chuck wood"

    word_list = phrase.split()

    assert len(word_list) == 13

    word_set = set(word_list)

    assert len(word_set) == 8

########
#
#  11. Page 18: Control Flow
#
########

@O.k
def p18_control_flow():

    """
    - Conditional controls are given by the keywords if, elif, and else
    - Ternary statements combine if-then-else statements onto one line
    - While loops are used by while <condition>:
    - For loops are used by for <variable> in <list>:
    - Finer controls can be used with continue and break
    """

    # Conditional controls are given by the keywords if, elif, and else

    def plus_minus_zero(number):
        if number > 0:
            return "Greater than zero"
        elif number < 0:
            return "Less than zero"
        else:
            return "Equal to zero"

    assert plus_minus_zero(1) == "Greater than zero"
    assert plus_minus_zero(-1) == "Less than zero"
    assert plus_minus_zero(0) == "Equal to zero"

    # Ternary statements combine if-then-else statements onto one line

    def vowel_checker(character):
        return "Vowel" if character in {'a', 'e', 'i', 'o', 'u'} else "Not Vowel"

    assert vowel_checker('e') == 'Vowel'
    assert vowel_checker('b') == 'Not Vowel'

    # While loops are used by while <condition>:

    counter_one = 0
    while counter_one < 10:
        counter_one += 1

    assert counter_one == 10

    # For loops are used by for <variable> in <list>:

    for counter_two in range(10):
        counter_two += 1

    assert counter_two == 10

    # Finer controls can be used with continue (go to next iteration) and break (quit loop)

    odds_below_five = set()

    for counter_three in range(10):
        if counter_three % 2 == 0:
            continue
        if counter_three == 5:
            break
        odds_below_five.add(counter_three)

    assert odds_below_five == {1, 3}

########
#
#  12. Page 19-20: Truthiness
#
########

@O.k
def p19to20_truthiness():

    """
    - Booleans are capitalized
    - None is similar to null in other languages
    - Falsy values are False, None, [], {}, "", set(), 0, and 0.0
    - Falsy values allow you to check for empty strings, lists, sets, etc
    - Lists have all and any functions to check if all elements or any elements are truthy
    """

    # Booleans are capitalized

    assert True
    assert not False

    # None is similar to null in other languages

    none_var = None
    assert none_var is None

    # Falsy values are False, None, [], {}, "", set(), 0, and 0.0

    assert not False
    assert not None
    assert not []
    assert not {}
    assert not ""
    assert not 0
    assert not 0.0

    # Falsy values allow you to check for empty strings, lists, sets, etc

    string_one = ""
    string_two = "Hello, World!"

    def bad_first_char(string):
        try:
            return string[0]
        except IndexError:
            return "Empty string"

    def good_first_char(string):
        return string and string[0]

    blank_bad_method = bad_first_char(string_one)
    hello_bad_method = bad_first_char(string_two)

    blank_good_method = good_first_char(string_one)
    hello_good_method = good_first_char(string_two)

    assert blank_bad_method == 'Empty string'
    assert hello_bad_method == 'H'

    assert blank_good_method == ''
    assert hello_good_method == 'H'

    # Lists have all and any functions to check if all elements or any elements are truthy

    all_true_list = [True, not None, [1], {1}, "1", 1, 1.0]
    some_true_list = [True, None, [1], {}, "1", 0, 1.0]
    none_true_list = [False, None, [], {}, "", 0, 0.0]

    assert all(all_true_list)
    assert any(all_true_list)

    assert not all(some_true_list)
    assert any(some_true_list)

    assert not all(none_true_list)
    assert not any(none_true_list)

########
#
#  13. Page 22: Sorting
#
########

@O.k
def p22_sorting():

    """
    - The sorted function is non-destructive, and returns a new list
    - Lists have a sort method that sorts in-place
    - Specifying reverse = True reverses the sort order
    - Specifying key = <function> compares according to the function results, as opposed to the values
    """

    # The sorted function is non-destructive, and returns a new list

    list_one = [4, 1, 2, 3]
    list_two = sorted(list_one)

    assert list_one != [1, 2, 3, 4]
    assert list_two == [1, 2, 3, 4]

    # Lists have a sort method that sorts in-place

    list_one.sort()

    assert list_one == list_two == [1, 2, 3, 4]

    # Specifying reverse = True reverses the sort order

    list_three = sorted(list_one, reverse = True)
    assert list_three == [4, 3, 2, 1]

    # Specifying key = <function> compares according to the function results, as opposed to the values

    students = [ { "id": 1, "fname": "Aaron", "lname": "Zapato"},
                 { "id": 2, "fname": "Benjamin", "lname": "Yarrow"},
                 { "id": 3, "fname": "Charles", "lname": "Xavier"} ]

    sorted_students = sorted(students, key = lambda student: student['lname'])

    assert sorted_students[0]['lname'] == 'Xavier'
    assert sorted_students[1]['lname'] == 'Yarrow'
    assert sorted_students[2]['lname'] == 'Zapato'

########
#
#  14. Page 23: List Comprehensions
#
########

########
#
#  15. Page 24: Generators and Iterators
#
########

########
#
#  16. Page 25: Randomness
#
########

########
#
#  17. Page 26: Regular Expressions
#
########

########
#
#  18. Page 27: Object-Oriented Programming
#
########

########
#
#  19. Page 28: Functional Tools
#
########

########
#
#  20. Page 29: Enumerate
#
########

########
#
#  21. Page 30: Zip and Argument Unpacking
#
########

########
#
#  22. Page 31-32: Args and Kwargs
#
########

if __name__ == "__main__":
    O.report()
