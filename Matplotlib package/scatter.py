from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#定义坐标轴
fig4 = plt.figure()
ax4 = plt.axes(projection='3d')

#生成三维数据
xx = np.random.random(20)*10-5   #取100个随机数，范围在5~5之间
yy = np.random.random(20)*10-5
X, Y = np.meshgrid(xx, yy)
Z = np.sin(np.sqrt(X**2+Y**2))

#作图
ax4.scatter(X,Y,Z,alpha=0.3,c=np.random.random(400),s=np.random.randint(10,20, size=(20, 40)))     #生成散点.利用c控制颜色序列,s控制大小

#设定显示范围

plt.show()