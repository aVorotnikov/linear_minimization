import math;

class Task:
    def __init__(self):
        self.count = 0

    @staticmethod
    def f(x):
        return x * math.sin(x) + 2 * math.cos(x)


    def f_count(self, x):
        self.count += 1
        return Task.f(x)


    def get_count(self):
        return self.count


    @staticmethod
    def limits():
        return (-5, -4)


    @staticmethod
    def accuracy():
        return [0.1, 0.01, 0.001];
