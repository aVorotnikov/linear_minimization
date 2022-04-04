from task import Task
import matplotlib.pyplot as plt
import numpy as np


(start, end) = Task.limits()
x_axe = np.arange(start, end + 0.001, 0.001)
x_min = -4.49340945790906

fig, ax = plt.subplots()
ax.plot(x_axe, np.array([Task.f(x) for x in x_axe]), [x_min], [Task.f(x_min)], 'd')
ax.set_xlim(xmin=x_axe[0] - 0.1, xmax=x_axe[-1] + 0.1)

ax.set_title('Function plot')
ax.legend(loc='upper left')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.grid(linestyle='dotted')
plt.legend(['function', 'min'])

plt.show()