def print_file(file_name):
    f = open(file_name)
    print('请输入需要显示该文件前几行：')

    count = int(input())
    save_list = []

    print('文件%s的前%d的内容如下：' % (file_name , count))
    for each_line in f:
        save_list.append(each_line)

    for i in range(count):
        print(save_list[i],end=' ')

file_name = input('请输入要打开的文件：')
print_file(file_name)

# def file_view(file_name, line_num):
#     print('\n文件%s的前%s的内容如下：\n' % (file_name, line_num))
#     f = open(file_name)
#     for i in range(int(line_num)):
#         print(f.readline(), end= '')
#
#     f.close()
#
# file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
# line_num = input('请输入需要显示该文件前几行：')
# file_view(file_name, line_num)
