import matplotlib.pyplot as plt
import numpy as np

# def Colormap(lst):
#
#     intensity = np.array(lst)
#
#     x, y = intensity.shape
#
#     x1 = range(0, x)
#     y1 = range(0, y)
#
#     x2,y2 = np.meshgrid(x1,y1)
#
#     print (x2,y2)
#
#     print (intensity.shape)
#
#     plt.pcolormesh(x2,y2,intensity)
#     plt.colorbar()
#     plt.savefig('colormap.pdf', dpi = 1200)
#     plt.show()

# def Colormap(lst):
#
#     intensity = np.array(lst)
#
#     x, y = intensity.shape
#
#     x1 = range(x+1) # changed this also
#     y1 = range(y+1) # changed this also
#
#     x2,y2 = np.meshgrid(x1,y1)
#
#     print(x2.shape,y2.shape)
#
#     print(intensity.shape)
#     print(np.swapaxes(intensity,0,1).shape)
#     plt.pcolormesh(x2,y2,np.swapaxes(intensity,0,1)) # Transpose of intensity
#     plt.colorbar()
#     # plt.savefig('colormap.pdf', dpi = 1200)
#     plt.show()

lst = np.random.randint(0,100, (16,1000))
intensity = np.array(lst)
print(intensity.shape)
x, y = intensity.shape
print(x,y)
x1 = range(0, x + 1)
y1 = range(0, y + 1)
print(x1,y1)
x2, y2 = np.meshgrid(x1, y1)
print(x2.shape)
print('---------')
print(y2.shape)
print('---------')
print(np.swapaxes(intensity, 0, 1).shape)
plt.pcolormesh(x2, y2, np.swapaxes(intensity, 0, 1))
plt.colorbar()
plt.show()