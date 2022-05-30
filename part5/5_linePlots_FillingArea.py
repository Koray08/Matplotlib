from matplotlib import pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')
# plt.xkcd()

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(dev_x))
# width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(x_indexes, dev_y, linestyle='--', color='#444444', linewidth="3", label="All Devs")

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(x_indexes, py_dev_y, color="#008fd5", label='Python')

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(x_indexes, js_dev_y, color="y", label="Javascript")

plt.xlabel("ages")
plt.ylabel("salary")
plt.title("Median Salary (USD) by age")

plt.fill_between(x_indexes, py_dev_y, alpha=0.25)

plt.legend()

plt.xticks(ticks=x_indexes, labels=dev_x)

plt.grid(True)

plt.tight_layout()

plt.savefig('plot.png')

plt.show()
