import numpy as np

point_grid = np.array([[0.0,0.0,0.0],[0.4,0.4,0.4],[0.8,0.8,0.8],[1.0,1.0,1.0]])
print(point_grid)

def func(x, y, z):
    return x*(1-x)*np.cos(4*np.pi*x) * (np.sin(4*np.pi*y**2)**2)*z

points = np.random.rand(10, 3)#实际点坐标
values = func(points[:,0], points[:,1],points[:,2])#实际点的值

from scipy.interpolate import griddata
grid_z0 = griddata(points, values, point_grid, method='nearest')
print(values)
print(points)