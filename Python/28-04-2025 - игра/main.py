player1 = 0
player2 = 0
status = True
print('Игроки вводят: камень(1), ножницы(2), бумага(3)')
while status:
    if player1 == 3:
        print('Выиграл игрок 1')
        print('Хотите сыграть снова?')
        answer = input()
        if answer == 'да':
            status = True
            player1 = 0
            player2 = 0
        else:
            status = False
    elif player2 == 3:
        print('выиграл игрок 2')
        print('Хотите сыграть снова?')
        answer = input()
        if answer == 'да':
            status = True
            player1 = 0
            player2 = 0
        else:
            status = False
    if status == False:
        break
    print('Ход первого игрока')
    p1_in = int(input())
    print('Ход второго игрока')
    p2_in = int(input())
    if (p1_in == 1 and p2_in == 2) or (p1_in == 2 and p2_in == 3) or (p1_in == 3 and p2_in == 1):
        player1+=1
        print('Игрок 1: ', player1, ' ', 'Игрок 2: ', player2)
    elif (p2_in == 1 and p1_in == 2) or (p2_in == 2 and p1_in == 3) or (p2_in == 3 and p1_in == 1):
        player2+=1
        print('Игрок 1: ', player1, ' ', 'Игрок 2: ', player2)
    elif p1_in == p2_in:
        print('Игрок 1: ', player1, ' ', 'Игрок 2: ', player2)