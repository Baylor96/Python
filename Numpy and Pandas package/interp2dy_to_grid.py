import numpy as np
import pandas as pd
from scipy.interpolate import griddata


def interp3d_to_grid(points, data, loc_range=[100,110,6291,6371], det_grid=1):

    lat_min = loc_range[0]
    lat_max = loc_range[1]
    lon_min = loc_range[2]
    lon_max = loc_range[3]

    lon_grid, lat_grid = np.meshgrid(np.arange(lon_min, lon_max + det_grid, det_grid),
                                     np.arange(lat_min, lat_max + det_grid, det_grid))

    grid_data = griddata(points, data, (lon_grid, lat_grid), method='linear')
    print(grid_data[0][0])

    if lat_grid[0, 0] < lat_grid[1, 0]:
        lat_grid = lat_grid[-1::-1]
        grid_data = grid_data[-1::-1]

    return [lon_grid, lat_grid, grid_data]

if __name__ == '__main__':

    vp = pd.read_excel('/Users/mac/PycharmProjects/Python/Numpy and Pandas package/vp.xlsx')

    latitude = np.array(vp['latitude'].values).reshape(-1,1)
    longitude = np.array(vp['longitude'].values).reshape(-1,1)
    depth = np.array(vp['depth'].values).reshape(-1, 1)
    vp = np.array(vp['vp'].values)

    point = np.concatenate([longitude, depth], axis=1)
    # print(point)

    new_vp = interp3d_to_grid(points=point, data=vp)
    print(new_vp)

