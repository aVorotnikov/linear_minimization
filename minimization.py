from methods import bisection as bs
from methods import golden_section as gs
from task import Task
import math


def method(solve):
    for eps in Task.accuracy():
        task = Task()
        x = solve(task, eps)
        print(str(eps) + ": " + "f(" + str(x) + ")=" + str(Task.f(x)) + "; f count: " + str(task.get_count()))


print("Bisection:")
method(bs.solve)
print("Predictions:")
(a, b) = Task.limits()
l = b - a
for eps in Task.accuracy():
    print(str(eps) + ": " + str(2 * (math.floor(math.log2(l / eps)) + 1)))

print("Golden section:")
method(gs.solve)
phi = (1 + math.sqrt(5)) / 2
print("Predictions:")
for eps in Task.accuracy():
    print(str(eps) + ": " + str(math.floor(math.log(l / eps, phi)) + 2))
