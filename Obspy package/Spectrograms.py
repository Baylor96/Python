import obspy
import os

PATH = './sacdata'
os.chdir(PATH)
for each_sac in os.listdir(os.curdir):
    sac = obspy.read(each_sac)
    name = os.path.splitext(each_sac)[0]
    sac.spectrogram(log=True, title=name)