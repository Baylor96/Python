def file_compare(file_name1, file_name2):
    f1 = open(file_name1)
    f2 = open(file_name2)
    count = 0
    differ = []

    for line1 in f1:
        line2 = f2.readline()
        count = count + 1
        if line1 != line2:
            differ.append(count)

    f1.close()
    f2.close()
    return differ

file_name1 = input('请输入需要比较的文件名：')
file_name2 = input('请输入需要比较的另一个文件名：')

differ = file_compare(file_name1, file_name2)

if len(differ) == 0:
    print('俩文件完全一样！')
else:
    print('俩文件共有【%d】处不同：' % len(differ))
    for each in differ:
        print('第%d行不一样' % each)
