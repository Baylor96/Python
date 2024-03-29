import obspy
import matplotlib.pyplot as plt
import numpy as np

sac = obspy.read('./data/3t.e.sac')
tr = sac[0]
threechannels = obspy.read('./data/3t.e.sac')
threechannels += obspy.read('./data/3t.n.sac')
threechannels += obspy.read('./data/3t.z.sac')
print(sac)

# # waveform plot
dt = tr.stats.starttime
sac.plot()
sac.plot(color='red', number_of_ticks=7, tick_rotation=5, tick_format='%I:%M %p', starttime=dt, endtime=dt + 120)
threechannels.plot(size = (800,600))

# # custom plotting
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.plot(tr.times('matplotlib'),tr.data,'b-')
# ax.xaxis_date()
# fig.autofmt_xdate()
# plt.show()

# filtering waveform
tr_filt = tr.copy()
tr_filt.filter('lowpass', freq=1.0, corners=2, zerophase=True)
t = np.arange(0, tr.stats.npts / tr.stats.sampling_rate, tr.stats.delta)
plt.subplot(211)
plt.plot(t,tr.data,'k',label='raw')
plt.ylabel('Raw data')
plt.legend()
plt.subplot(212)
plt.plot(t,tr_filt.data,'r',label='Lowpass')
plt.ylabel('Lowpass Data')
plt.xlabel('Time[s]')
plt.suptitle(tr.stats.starttime)
plt.legend()
plt.show()