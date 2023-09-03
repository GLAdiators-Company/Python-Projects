import random
draw = 0
win = 0
lose = 0
i = 0
enities = [1,2,3]
while(i<3):
    try:
        a = int(input('[1] -> Snake\n[2] -> Water\n[3] -> Gun\nYour input -> '))
        ci = random.randint(1,3)
        if(a==ci):
            print(f'Draw!\nComputer input is {ci}\n')
            draw +=1
        elif(a==1 and ci==2 or a==2 and ci==3 or a==3 and ci==1):
            print(f'You win\nComputer input is {ci}\n')
            win +=1
        elif(a not in enities):
            print('INVALID INPUT !\n')
            i -= 1
        else:
            print(f'You lose!\nComputer input is {ci}\n')
            lose +=1
        i += 1
    except Exception  as e:
        print('Enter only integer value . . \n')

print('====== Final Results ======'.center(50))
print()

if(draw == 2):
    print('Draw'.center(50))
elif(win == 2):
    print('You win! '.center(50))
else:
    print('You lose !'.center(50))
print()

