from random import randint
num = randint(0,1000)

print('Guess what am I thinking')
answer = eval(input())
print(answer)

while answer != num:

    if answer < num:
        print("%d Too Small" % answer)
        answer = eval(input())

    if answer > num:
        print("%d Too Big" % answer)
        answer = eval(input())

print("Bingo")
