def solve(task, eps):
    (a, b) = task.limits()
    m = (a + b) / 2
    return (m, task.f_count(m))