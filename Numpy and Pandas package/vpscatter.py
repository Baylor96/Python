import pandas as pd
import numpy as np
from scipy import interpolate

def interp3d_to_grid(points, data):

    det_grid = 0.5
    detd_grid = 1
    loc_range = [30.5, 43.5, 100.5, 109.5, 6306, 6371]

    lat_min = loc_range[0]
    lat_max = loc_range[1]
    lon_min = loc_range[2]
    lon_max = loc_range[3]
    depth_min = loc_range[4]
    depth_max = loc_range[5]

    lon_grid, lat_grid, dep_grid = np.meshgrid(
        np.arange(lon_min, lon_max + det_grid, det_grid),
        np.arange(lat_min, lat_max + det_grid, det_grid),
        np.arange(depth_min, depth_max, detd_grid)
    )

    grid_data = interpolate.griddata(points, data, (lon_grid, lat_grid, dep_grid), method='nearest')
    print((lon_grid[0][0][0], lat_grid[0][0][0], dep_grid[0][0][60]))
    print(grid_data[0][0][60])
    # grid_data = grid_data[:, :, 0]

    # if lat_grid[0, 0] < lat_grid[1, 0]:
    #     lat_grid = lat_grid[-1::-1]
    #     grid_data = grid_data[-1::-1]

    return [lat_grid, lon_grid, dep_grid, grid_data]


if __name__ == '__main__':

    vp = pd.read_excel('/Users/mac/PycharmProjects/Python/Numpy and Pandas package/vp.xlsx')

    latitude = np.array(vp['latitude'].values).reshape(-1,1)
    longitude = np.array(vp['longitude'].values).reshape(-1,1)
    depth = np.array(vp['depth'].values).reshape(-1,1)
    vp = np.array(vp['vp'].values)

    point = np.concatenate([latitude, longitude, depth], axis=1)

    new_vp = interp3d_to_grid(points=point, data=vp)
    # print(new_vp[0])

    # data_df = pd.DataFrame(new_vp)
    #
    # data_df.columns = ['A', 'B', 'C', 'D']
    #
    # writer = pd.ExcelWriter('hhh.xlsx')
    # data_df.to_excel(writer, 'page_1',float_format='%.5f')
    # writer.save()




