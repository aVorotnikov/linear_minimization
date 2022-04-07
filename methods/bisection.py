def solve(task, eps):
    (a, b) = task.limits()
    delta = eps / 100
    while b - a >= eps:
        m = (a + b) / 2
        left = task.f_count(m - delta)
        right = task.f_count(m + delta)
        if (left < right):
            b = m + delta
        else:
            a = m - delta
    return (a + b) / 2