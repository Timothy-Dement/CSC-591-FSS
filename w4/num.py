from math import inf, sqrt
from sample import Sample


class Num:

    def __init__(self, max_size=512):

        self.count = 0
        self.mean = 0
        self.m2 = 0
        self.standard_deviation = 0
        self.lo = inf
        self.hi = -inf
        self.sample = Sample(max_size)

    def num_inc(self, new):

        self.count += 1

        self.sample.sample_inc(new)

        delta = new - self.mean

        self.mean += delta / self.count

        self.m2 += delta * (new - self.mean)

        if new > self.hi:
            self.hi = new

        if new < self.lo:
            self.lo = new

        if self.count > 1:
            self.standard_deviation = sqrt(self.m2 / (self.count - 1 + 10 ** -32))

    def nums(self, num_list):

        for num in num_list:
            self.num_inc(num)

    def num_dec(self, remove):

        if not self.count == 1:

            self.count -= 1

            delta = remove - self.mean

            self.mean -= delta / self.count

            self.m2 -= delta * (remove - self.mean)

            if self.count > 1:
                self.standard_deviation = sqrt(self.m2 / (self.count - 1 + 10 ** -32))

    def num_norm(self, x):

        return (x - self.lo) / (self.hi - self.lo + 10 ** -32)

    def num_xpect(self, other):

        count_sum = self.count + other.count + 10 ** -32

        return self.count / count_sum * self.standard_deviation + \
               other.count / count_sum * other.standard_deviation
