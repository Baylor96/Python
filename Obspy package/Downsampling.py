import numpy as np
import matplotlib.pyplot as plt
import obspy

sac = obspy.read('./sacdata/CA.1563A.01.HHE.sac')
tr = sac[0]
tr_new = tr.copy()
tr_new.decimate(factor=4,strict_length=False)
tr_filt = tr.copy()
tr_filt.filter('lowpass',freq = 0.4 * tr.stats.sampling_rate/4.0)
t = np.arange(0,tr.stats.npts / tr.stats.sampling_rate, tr.stats.delta)
t_new = np.arange(0, tr_new.stats.npts / tr_new.stats.sampling_rate, tr_new.stats.delta)
# plt.subplot(311)
plt.plot(t, tr.data, 'k', label='raw', alpha = 0.3)
# plt.subplot(312)
plt.plot(t, tr_filt.data, 'b', label = 'lowpassed', alpha = 0.7)
# plt.subplot(313)
plt.plot(t_new, tr_new.data, 'r', label = 'downsampled', alpha = 0.7)
plt.xlabel('Time[s]')
plt.suptitle(tr.stats.starttime)
plt.show()