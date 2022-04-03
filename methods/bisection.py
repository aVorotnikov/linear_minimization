def solve(task, eps):
    (a, b) = task.limits()
    while b - a > eps:
        m = (a + b) / 2
        left = task.f_count(m - task.get_delta())
        right = task.f_count(m + task.get_delta())
        if (left < right):
            b = m
        else:
            a = m
    m = (a + b) / 2
    return (m, task.f_count(m))