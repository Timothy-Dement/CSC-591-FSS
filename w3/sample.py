from math import ceil
from random import random, randrange


class Sample:

    def __init__(self, m):

        self.maximum_size = m
        self.add_attempts = 0
        self.sorted = False
        self.sample_list = []

    def sample_inc(self, new):

        self.add_attempts += 1

        current_size = len(self.sample_list)

        if current_size < self.maximum_size:

            self.sorted = False
            self.sample_list.append(new)

        elif random() < current_size / self.add_attempts:

            self.sorted = False
            self.sample_list[randrange(current_size)] = new

    def sample_sorted(self):

        if not self.sorted:
            self.sample_list.sort()
            self.sorted = True

    def nth(self, percentile):

        self.sample_sorted()

        current_size = len(self.sample_list)

        return self.sample_list[ceil(current_size * percentile) - 1]

    def nths(self, percentiles=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]):

        results = []

        for percentile in percentiles:
            results.append(self.nth(percentile))

        return results