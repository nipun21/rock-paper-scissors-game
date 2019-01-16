# Game Rule ::- Rock beats scissors   and  paper beats rock
from random import randint
m=1
n=1
while(m<6):
    player = input('rock(r), paper(p) or scissors(s)?')
    chosen=randint(1,3)
    if(chosen == 1):
      chosen='r'
    elif(chosen == 2):
      chosen='p'
    elif(chosen == 3):
      chosen='s' 
    print(player,' Vs ',chosen)

    if(player == chosen):
        print('Draw!!',n)
        n=n+1
    elif(player == 'p' and chosen=='r'):
        print('Gotcha You Win!!')
    elif(player == 'p' and chosen=='s'):
        print('Gotcha You Win!!')
    elif(player == 'r' and chosen=='s'):
        print('Gotcha You Win!!')
    elif(player == 'r' and chosen=='p'):
        print('Oohh You Lose!!',m)
        m=m+1
    elif(player == 's' and chosen=='r'):
        print('Oohh You Lose!!',m)
        m=m+1
    elif(player == 's' and chosen=='p'):
        print('Oohh You Lose!!',m)
        m=m+1
    if(m > 5):
        print('Game Over!!')
