import numpy as np
import matplotlib.pyplot as plt


def plot_scatter(x1, y1, x2, y2):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(xmax=9, xmin=0)
    plt.ylim(ymax=9, ymin=0)
    plt.grid(linestyle="--")

    colors1 = '#00CED1'
    colors2 = '#DC143C'
    area = np.pi * 4 ** 2

    plt.scatter(x1, y1, s=area, c=colors1, alpha=0.4, label='陈健龙1')
    plt.scatter(x2, y2, s=area, c=colors2, alpha=0.4, label='陈健龙2')
    plt.plot([0, 9.5], [9.5, 0], linewidth='0.5', color='#000000')
    plt.legend(loc=2)
    plt.savefig('12345.png', dpi=300)
    plt.show()


if __name__ == '__main__':
    x1 = np.random.normal(2, 1.2, 300)
    y1 = np.random.normal(2, 1.2, 300)
    x2 = np.random.normal(7.5, 1.2, 300)
    y2 = np.random.normal(7.5, 1.2, 300)

    plot_scatter(x1, y1, x2, y2)