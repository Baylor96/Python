def save_file(file_name):
    f = open(file_name,'w')
    print('请输入要写的内容【:w保存退出】：')

    while True:
        content = input()
        if content == ':w':
            break
        else:
            f.write('%s\n' % content)

    f.close()


file_name = input('请输入一个文件名:')
save_file(str(file_name) + '.txt')