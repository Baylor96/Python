import obspy
import os

PATH = './sacdata'
os.chdir(PATH)
for each_sac in os.listdir(os.curdir):
    sac = obspy.read(each_sac)
    tr = sac[0]
    samprate = tr.stats.sampling_rate
    name = os.path.splitext(each_sac)[0]
    sac.spectrogram(log=True, title=name, clip=[0,0.5], outfile=name + '.png', fmt='png')