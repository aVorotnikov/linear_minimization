import math


def solve(task, eps):
    (a, b) = task.limits()
    phi = (1 + math.sqrt(5)) / 2
    m = b - (b - a) / phi
    return (m, task.f_count(m))