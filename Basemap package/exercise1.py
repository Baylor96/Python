from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Default value of projection is cyl--cylindrical Equidistant projection/Equirectangular
# projection/Plate carree
map = Basemap(projection='cyl')

# Many projection modes require additional parameters
# map = Basemap(projection='ortho', lat_0=0, lon_0=0)
map = Basemap(projection='aeqd', lat_0=50, lon_0=10)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

plt.show()