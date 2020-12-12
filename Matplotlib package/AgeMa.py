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

ax = plt.gca()
ax.xaxis.set_ticks_position('top')
ax.yaxis.set_ticks_position('left')
ax.invert_xaxis()
ax.invert_yaxis()

plt.xlabel('O18')
plt.ylabel('Age')
plt.scatter(x, y, c=np.random.random(10801))
plt.show()