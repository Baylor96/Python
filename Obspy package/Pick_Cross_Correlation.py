from __future__ import print_function

import obspy

from obspy.signal.cross_correlation import xcorr_pick_correction

# read example data of two small earthquakes

path = "https://examples.obspy.org/BW.UH1..EHZ.D.2010.147.%s.slist.gz"

st1 = obspy.read(path % ("a",))

st2 = obspy.read(path % ("b",))

tr1 = st1.select(component="Z")[0]

tr2 = st2.select(component="Z")[0]

t1 = obspy.UTCDateTime("2010-05-27T16:24:33.315000Z")

t2 = obspy.UTCDateTime("2010-05-27T16:27:30.585000Z")

dt, coeff = xcorr_pick_correction(t1, tr1, t2, tr2, 0.05, 0.2, 0.1, plot=True)

print("No preprocessing:")

print("  Time correction for pick 2: %.6f" % dt)

print("  Correlation coefficient: %.2f" % coeff)

dt, coeff = xcorr_pick_correction(t1, tr1, t2, tr2, 0.05, 0.2, 0.1, plot=True,

                                  filter="bandpass",

                                  filter_options={'freqmin': 1, 'freqmax': 10})

print("Bandpass prefiltering:")

print("  Time correction for pick 2: %.6f" % dt)

print("  Correlation coefficient: %.2f" % coeff)