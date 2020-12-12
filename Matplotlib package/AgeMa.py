import pandas
import matplotlib.pyplot as plt
import numpy as np
import os

data_path = os.path.join(os.path.dirname(__file__), 'data.xls')
data = pandas.read_excel(data_path)

print(data.columns)

x = data['d18O   ']
y = data['Best_AgeMa']

figure = plt.figure(figsize=(5, 10))

# plt.xlim(0,5)
plt.ylim(0,70)
plt.xlabel('O18')
plt.ylabel('Age')
plt.scatter(x, y, c=np.random.random(10801))
parameter = np.polyfit(x, y, 6)
y2 = parameter[0] * x ** 6 + parameter[1] * x ** 5 + parameter[2] * x ** 4 + \
     parameter[3] * x ** 3 + parameter[4] * x ** 2 + parameter[5] * x + parameter[6]
plt.plot(x, y2, color='r')

ax = plt.gca()
ax.xaxis.set_ticks_position('top')
ax.yaxis.set_ticks_position('left')
ax.invert_xaxis()
ax.invert_yaxis()

plt.show()