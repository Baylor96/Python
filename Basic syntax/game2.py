import random
answer = random.randint(1,10)
print('-----------------------------------------')
temp = input("不放猜一下，我现在心里想的是那个数字：")
guess = int(temp)
if guess == answer:
    print("歪日，你是我心里的蛔虫吗？")
    print("哼，猜中了也没用！")
else:
    if guess > answer:
        print('大了大了~~')
    else:
        print('小了小了~~')
while guess != answer:
    temp = input("哎呀，猜错了，请重新输入：")
    guess = int(temp)
    if guess == answer:
        print("歪日，你是我心里的蛔虫吗？")
        print("哼，猜中了也没用！")
    else:
        if guess > answer:
            print('大了大了~~')
        else:
            print('小了小了~~')
print("猜对啦！游戏结束，不玩啦^_^")