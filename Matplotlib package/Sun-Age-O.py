import pandas
import matplotlib.pyplot as plt
import os

data_path = os.path.join(os.path.dirname(__file__), 'data.xls')
data = pandas.read_excel(data_path)

print(data.columns)

x = data['d18O   ']
y = data['Best_AgeMa']

plt.xlabel('O')
plt.ylabel('Age')
plt.scatter(x, y)
plt.show()