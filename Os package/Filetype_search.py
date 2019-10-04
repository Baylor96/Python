import os

def search_file(start_dir, target):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            Search_list.append(os.getcwd() + os.sep + each_file + os.linesep)
        if os.path.isdir(each_file):
            search_file(each_file, target)
            os.chdir(os.pardir)

start_dir = input('请输入待查找的初始目录：')
target_input = input('请输入查找文件格式：')
Target = []
Target.append(target_input)
print(Target)
# target = ['.mp4', '.avi', '.rmvb']
Search_list = []

search_file(start_dir, Target)
print(Search_list)

f = open(os.getcwd() + os.sep + 'Search_List.txt', 'w')
f.writelines(Search_list)
f.close()