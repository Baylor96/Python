import numpy as np
from scipy.signal import hilbert
import matplotlib.pyplot as plt
from obspy.signal.tf_misfit import plot_tfr, plot_tf_misfits

tmax = 6.
dt = 0.01
npts = int(tmax / dt + 1)
t = np.linspace(0., tmax, npts)

fmin = .5
fmax = 10

A1 = 4.
t1 = 2.
f1 = 2.
phi1 = 0.

H1 = (np.sign(t - t1) + 1) / 2
st1 = A1 * (t - t1) * np.exp(-2 * (t - t1))
st1 *= np.cos(2. * np.pi * f1 * (t - t1) + phi1 * np.pi) * H1

plot_tfr(st1, dt=dt, fmin=fmin, fmax=fmax)

phase_shift = 0.1
amp_fac = 1.1

st2 = st1.copy()

st1p = hilbert(st1)
st1p = np.real(np.abs(st1p) * \
        np.exp((np.angle(st1p) + phase_shift * np.pi) * 1j))

# signal with amplitude error
st1a = st1 * amp_fac

plot_tf_misfits(st1a, st2, dt=dt, fmin=fmin, fmax=fmax, show=False)
# plot_tf_misfits(st1p, st2, dt=dt, fmin=fmin, fmax=fmax, show=False)

plt.show()