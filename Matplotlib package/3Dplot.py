import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax1 = plt.axes(projection='3d')
# ax = fig.add_subplot(111,projection='3d')

z = np.linspace(0,13,1000)
x = 5*np.sin(z)
y = 5*np.cos(z)
zd = 13*np.random.random(100)
xd = 5*np.sin(zd)
yd = 5*np.cos(zd)
ax1.scatter3D(xd,yd,zd, cmap='Blues')
ax1.plot3D(x,y,z,'gray')
plt.show()

fig = plt.figure()
ax3 = plt.axes(projection='3d')

xx = np.arange(-5, 5, 0.1)
yy = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(xx, yy)
Z = np.sin(X)+np.cos(Y)

ax3.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
ax3.contour(X, Y, Z, offset=-2, cmap='rainbow')
plt.show()