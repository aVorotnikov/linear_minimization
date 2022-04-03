from methods import bisection as bs
from methods import golden_section as gs
from task import Task


def method(solve):
    for eps in Task.accuracy():
        task = Task()
        (x, f) = solve(task, eps)
        print(str(eps) + ": " + "f(" + str(x) + ")=" + str(f) + "; f count: " + str(task.get_count()))


print("Bisection:")
method(bs.solve)

print("Golden section:")
method(gs.solve)
