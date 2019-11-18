import obspy
import matplotlib.pyplot as plt
import numpy as np

sac = obspy.read('./sacdata/CA.1563A.01.HHE.sac')
tr = sac[0]
threechannels = obspy.read('./sacdata/CA.1563A.01.HHE.sac')
threechannels += obspy.read('./sacdata/CA.1563A.01.HHN.sac')
threechannels += obspy.read('./sacdata/CA.1563A.01.HHZ.sac')
print(sac)

# # waveform plot
# dt = tr.stats.starttime
# sac.plot()
# sac.plot(color='red', number_of_ticks=7, tick_rotation=5, tick_format='%I:%M %p', starttime=dt, endtime=dt + 120)
# threechannels.plot(size = (800,600))

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
plt.plot(t,tr.data,'k')
plt.ylabel('Raw data')
plt.subplot(212)
plt.plot(t,tr_filt.data,'r')
plt.ylabel('Lowpass Data')
plt.xlabel('Time[s]')
plt.suptitle(tr.stats.starttime)
plt.show()