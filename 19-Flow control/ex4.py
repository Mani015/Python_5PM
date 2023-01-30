print('WELCOME TO CANDY CRUSH')
game=eval(input('enter level number:'))
if game==1 :
    print('level one is completed')
    game=int(input('you are going to second level:'))
    if game==2:
        print('level two is completed')
        game = int(input('you are going to third level:'))
        if game==3:
            print('level three is completed')
            game = int(input('you are going to fourth level:'))
            if game==4:
                print('level four is completed')
            else:
                print('level 4 is unsatisfied')
        else:
            print('level 3 is unsatisfied')
    else:
        print('level 2 is unsatisfied')
else:
    print('level 1 is unsatisfied')
print('game is completed')
print('PLAY AGAIN')
