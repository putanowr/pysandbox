import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm
import matplotlib.colors
import matplotlib
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
if __name__ == '__main__':
    #matplotlib.use('Qt5Agg')
    resolution = (10,10,10)
    sides = (1.0, 1.0, 1.0)
    line_grids = []
    for side_len, res in zip(sides, resolution):
        line_grids.append(np.linspace(0, side_len, res))

    xx,yy,zz = np.meshgrid(*line_grids)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    cmap = matplotlib.cm.get_cmap(name='jet', lut=40)
    norm = matplotlib.colors.Normalize()
    mappable = matplotlib.cm.ScalarMappable(cmap=cmap, norm=norm)
    val = xx**2 + yy**2 + zz**2

    #ax.scatter(xx.reshape(-1,), yy.reshape(-1,), zz.reshape(-1,), alpha=0.9, s=180, c=val.reshape(-1,), cmap=cmap, norm=norm)

    u = np.linspace(0, 2 * np.pi, 24)
    v = np.linspace(0, np.pi, 12)

    X = 0.05 * np.outer(np.cos(u), np.sin(v))
    Y = 0.05 * np.outer(np.sin(u), np.sin(v))
    Z = 0.05 * np.outer(np.ones(np.size(u)), np.cos(v))
    mappable.set_array(val.reshape(-1,))
    mappable.autoscale()

    for x,y,z,v in zip(xx.reshape(-1,), yy.reshape(-1,), zz.reshape(-1,), val.reshape(-1,)):
        Xc = X + x
        Yc = Y + y
        Zc = Z + z
        c = mappable.to_rgba(v, alpha=1.0)
        ax.plot_surface(Xc,Yc,Zc, color=c, edgecolor='none', antila)
    plt.show()



