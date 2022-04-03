import math


def solve(task, eps):
    phi = (1 + math.sqrt(5)) / 2
    (a, b) = task.limits()
    a1 = b - (b - a) / phi
    fa = task.f_count(a1)
    need_eval_b = True
    while b - a >= eps:
        if need_eval_b:
            b1 = a + (b - a) / phi
            fb = task.f_count(b1)
        else:
            a1 = b - (b - a) / phi
            fa = task.f_count(a1)
        if fa > fb:
            a = a1
            need_eval_b = True
            a1 = b1
            fa = fb
        else:
            b = b1
            need_eval_b = False
            b1 = a1
            fb = fa
    return (a + b) / 2