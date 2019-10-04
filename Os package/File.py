def save_file(fish1, fish2, count):
    file_name_old = 'old_' + str(count) + '.txt'
    file_name_young = 'young_' + str(count) + '.txt'

    old_file = open(file_name_old, 'w')
    young_file = open(file_name_young, 'w')

    old_file.writelines(fish2)
    young_file.writelines(fish1)

    old_file.close()
    young_file.close()

def split_file(file_name):
    f = open('record.txt')

    fish1 = []
    fish2 = []
    count = 1

    for each_line in f:
        if each_line[:6] != '======':
            (role,line_spoken) = each_line.split(':',1)
            if role == '小甲鱼':
                fish1.append(line_spoken)
            if role == '小客服':
                fish2.append(line_spoken)
        else:
            save_file(fish1, fish2, count)

            fish1 = []
            fish2 = []
            count = count + 1

    save_file(fish1, fish2, count)
    f.close()

split_file('demo.txt')
