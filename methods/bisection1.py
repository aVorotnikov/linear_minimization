def solve(task, eps):
    (a, b) = task.limits()
    parity = False
    while b - a >= eps:
        parity = not parity
        if parity:
            a1 = (5 * a + 3 * b) / 8
            b1 = (3 * a + 5 * b) / 8
            fa = task.f_count(a1)
            fb = task.f_count(b1)
            if fa > fb:
                a = (a + b) / 2
                a1 = b1
                fa = fb
                need_eval_b = True
            else:
                b = (a + b) / 2
                b1 = a1
                fb = fa
                need_eval_b = False
            continue
        if need_eval_b:
            b1 = (a + 3 * b) / 4
            fb = task.f_count(b1)
        else:
            a1 = (3 * a + b) / 4
            fa = task.f_count(a1)
        if fa > fb:
            a = (a + b) / 2
        else:
            b = (a + b) / 2
    return (a + b) / 2