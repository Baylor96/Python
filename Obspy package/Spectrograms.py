import obspy
import os


def sac_threechannel(sac_path, station, flag):

    station_channel_E = station + '.e.sac'
    station_channel_N = station + '.n.sac'
    station_channel_Z = station + '.z.sac'

    Data_path_E = os.path.join(sac_path, station_channel_E)
    Data_path_N = os.path.join(sac_path, station_channel_N)
    Data_path_Z = os.path.join(sac_path, station_channel_Z)

    st = obspy.read(Data_path_Z)
    st += obspy.read(Data_path_N)
    st += obspy.read(Data_path_E)

    start_time = st[0].stats.starttime
    end_time = st[0].stats.endtime
    duration = end_time - start_time
    print('duration:{}'.format(duration))

    if flag == 1:
        for i in range(3):
            tr = st[i]
            tr.trim(start_time, start_time + 120)

    st.plot(size=(800,600))

    return st


if __name__ == '__main__':

    input_path = os.path.join(os.path.dirname(__file__), 'data')

    sac_path = os.path.join(input_path, '3t.e.sac')

    station = '3t'

    st = sac_threechannel(input_path, station, flag=False)

    st.spectrogram(log=True, title=station, clip=[0,0.5], outfile=station + '.png', fmt='png')