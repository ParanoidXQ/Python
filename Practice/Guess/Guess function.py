def isEqual(num1, num2):
    if num1 < num2:
        print("%d Too Small" % num1)
        return False

    elif num1 > num2:
        print("%d Too Big" % num1)
        return False

    else:
        print("Bingo!")
        return True


from random import randint

num = randint(0, 100)

name = input('请输入你的名字：')  # 输入玩家名字
f = open('F:\PROJECT\Python\Practice\Guess\game1.txt')
lines = f.readlines()  # 行读取文件
f.close()
scores = {}  # 初始化字典
for i in lines:
    s = i.split()  # 分割每一行为list
    print(s)
    scores[s[0]] = s[1:]  # 第一项为key 剩下的为value value为list
score = scores.get(name)  # 查找当前玩家数据 为list 即scores的value
if score is None:
    score = [0, 0, 0]

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times > 0:
    ave_times = float(total_times) / game_times
else:
    ave_times = 0
print('%s，你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (name, game_times, min_times, ave_times))

print('Guess what am I thinking')
Bingo = False
times = 0
while Bingo != True:
    times += 1
    answer = eval(input())
    Bingo = isEqual(answer, num)

if game_times == 0 or times < min_times:
    min_times = times
total_times += times
game_times += 1

# 成绩更新到文件
scores[name] = [str(game_times), str(min_times), str(total_times)] # 由于f.write()函数只能写入字符串或字符串变量
print(scores)
result = ''  # 定义result为空字符串
for n in scores:
    line = n + ' ' + ' '.join(scores[n]) + '\n'  # 合成字符串
    result += line  # 写入字符串
    print(result)

# 写入
f = open('F:\PROJECT\Python\Practice\Guess\game1.txt', 'w')
f.write(result)
f.close()
