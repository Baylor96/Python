from obspy.taup import TauPyModel

model = TauPyModel(model="ak135")

arrivals = model.get_ray_paths(source_depth_in_km=20,
                               distance_in_degree=10,
                               phase_list=["P"])

ax = arrivals.plot_rays(plot_type="cartesian")

arrivals = model.get_pierce_points(20, 10)

print(arrivals[0])
print(arrivals[0].pierce['time'])
print(arrivals[0].pierce['depth'])

arrivals = model.get_travel_times(source_depth_in_km=0,
                                  distance_in_degree=10)
print(arrivals)