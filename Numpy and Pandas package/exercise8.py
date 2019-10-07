import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# # Series
# data = pd.Series(np.random.randn(1000),index=np.arange(1000))
# data = data.cumsum()
# print(data)

# DataFrame
data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list("ABCD"))
print(data.head())
data = data.cumsum()

# plot methods:
# 'bar', 'hist', 'box', 'kde', 'area', scatter', hexbin', 'pie'

ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
data.plot.scatter(x='A',y='C',color='DarkGreen',label='Class2',ax=ax)
plt.show()