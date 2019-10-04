# f = open('OpenMe.mp3')
# for each_line in f:
#         print(each_line,end=' ')
# f.close()

# f1 = open('OpenMe.mp3')
# f2 = open('OpenMe.txt', 'x')        # 使用”x”打开更安全
# f2.write(f1.read())
# f2.close()
# f1.close()

f = open('OpenMe.txt')
file = f.read(4)
print(file)
f.close()