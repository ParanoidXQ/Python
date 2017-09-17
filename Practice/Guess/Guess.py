from random import randint
num = randint(0,1000)

print('Guess what am I thinking')
answer = eval(input())
print(answer)

while answer != num:

    if answer < num:
        print("Too Small")
        answer = eval(input())

    if answer > num:
        print("Too Big")
        answer = eval(input())

print("Bingo")
