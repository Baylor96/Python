import numpy as np
import matplotlib.pyplot as plt
import obspy.signal

st = obspy.read('./sacdata/CA.WT74.01.HHE.sac')
data = st[0].data
npts = st[0].stats.npts
samprate = st[0].stats.sampling_rate
print(npts,samprate,st[0].stats.delta)

st_filt = st.copy()
st_filt.filter('bandpass', freqmin=10, freqmax=20, corners=2, zerophase=True)
data_envelope = obspy.signal.filter.envelope(st_filt[0].data)
t = np.arange(0, npts / samprate, 1 / samprate)

plt.plot(t, st_filt[0].data, 'k')
plt.plot(t, data_envelope, 'r')
plt.title(st[0].stats.starttime)
plt.ylabel('Filtered Data w/ Envelope')
plt.xlabel('Time [s]')
plt.show()