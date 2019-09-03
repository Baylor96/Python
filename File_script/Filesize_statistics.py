import os

all_files = os.listdir(os.curdir) # 使用os.curdir表示当前目录更标准
file_dict = dict()

for each_file in all_files:
    if os.path.isfile(each_file):
        file_size = os.path.getsize(each_file)
        file_dict[each_file] = file_size

for each in file_dict.items():
    print('%s【%dBytes】' % (each[0], each[1]))