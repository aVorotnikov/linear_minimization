from methods import bisection as bs
from methods import golden_section as gs
from task import Task


def method(solve):
    for eps in Task.accuracy():
        task = Task()
        x = solve(task, eps)
        print(str(eps) + ": " + "f(" + str(x) + ")=" + str(Task.f(x)) + "; f count: " + str(task.get_count()))


print("Bisection:")
method(bs.solve)

print("Golden section:")
method(gs.solve)
