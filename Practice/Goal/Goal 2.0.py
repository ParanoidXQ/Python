from random import choice

score = [0, 0]
direction = ['left', 'right', 'center']


def kick():
    print('-----You Kick!-----')
    print('choose one direction')
    print('left', 'right', 'center')
    you = input()
    print('You chose the ' + you)
    com = choice(direction)
    print('goalkeeper saved ' + com)
    if you != com:
        print('Goal!')
        score[0] += 1
    else:
        print('You Miss!')
    print('The socre is %d vs %d' % (score[0], score[1]))

    print('-----You Save!-----')
    print('choose one direction')
    print('left', 'right', 'center')
    you = input()
    print('You chose the ' + you)
    com = choice(direction)
    print('Computer kicked ' + com)
    if you != com:
        print('Saved!')
    else:
        print('You Miss!')
        score[1] += 1
    print('The socre is %d vs %d' % (score[0], score[1]))


for i in range(5):
    print('==== Round %d ====' % (i + 1))
    kick()

while (score[0] == score[1]):
    i += 1
    print('==== Round %d ====' % (i + 1))
    kick()

if score[0] > score[1]:
    print('You Win!')
else:
    print('You Lose!')
