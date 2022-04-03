from task import Task
import matplotlib.pyplot as plt
import numpy as np


(start, end) = Task.limits()
x_axe = np.arange(start, end, 0.001)

fig, ax = plt.subplots()
ax.plot(x_axe, np.array([Task.f(x) for x in x_axe]))
ax.set_xlim(xmin=x_axe[0] - 0.1, xmax=x_axe[-1] + 0.1)

ax.set_title('Function graph')
ax.legend(loc='upper left')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.grid()
plt.legend(['function'])

plt.show()