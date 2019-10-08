import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.xlim((-1, 2))
plt.ylim((-2, 3))

new_sticks = np.linspace(-1, 2, 5)
plt.xticks(new_sticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

l1, = plt.plot(x,y2,label='up')
l2, = plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')
plt.legend(handles=[l1,l2],labels=['aaa','bbb'],loc='upper right')

plt.show()