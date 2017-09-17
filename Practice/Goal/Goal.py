from random import choice

Gk_P = 0
Pl_P = 0
direction = ['left', 'right', 'center']
while Gk_P < 3 and Pl_P < 3:
    print("Chose one direction:")
    print("left, right, center")
    kick = input()
    GK = choice(direction)
    print("The goalkeeper choose the %s direction" % GK)
    if GK == kick:
        print('You Lose!')
        Gk_P += 1
    else:
        print("You Win!")
        Pl_P += 1

if Gk_P == 3:
    winner = "gaolkeeper"
else:
    winner = 'YOU'
print('The winner is %s' % winner)
