import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
if __name__ == '__main__':
    #matplotlib.use('Qt5Agg')
    resolution = (10,10, 10)
    sides = (0.1, 0.1, 0.1)
    line_grids = []
    for side_len, res in zip(sides, resolution):
        line_grids.append(np.linspace(0, side_len, res))

    xx,yy,zz = np.meshgrid(*line_grids)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    cmap = matplotlib.cm.get_cmap(name='jet', lut=40)
    norm = matplotlib.colors.Normalize()
    val = xx**2 + yy**2 + zz**2
    ax.scatter3D(xx.reshape(-1,), yy.reshape(-1,), zz.reshape(-1,), alpha=0.9, s=180, c=val.reshape(-1,), cmap=cmap, norm=norm)

    plt.show()



