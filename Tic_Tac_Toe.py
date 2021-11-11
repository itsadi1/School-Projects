m,n,repeated=[],1,False

tic_tac ={(1,1):'-',
          (1,2):'-',
          (1,3):'-',
          (2,1):'-',
          (2,2):'-',
          (2,3):'-',
          (3,1):'-',
          (3,2):'-',
          (3,3):'-'}



while True:
    
    if n==1:
        x = input(f'Enter Position Player {n}: ')
        n=2
        a,b = int(x[0]),int(x[-1])
        tic_tac[(a,b)]='x'

    else:
        x = input(f'Enter Position Player {n}: ')
        n=1
        a,b = int(x[0]),int(x[-1])
        tic_tac[(a,b)]='o'

    if a>3 or b >3:
        print("!!index out of range.!!")

    for i in m:

        if i==x:
            repeated=True
            print('values_repeated')
            quit()
            break

    if repeated==False:
        m.append(x)

    for i in range(1,4):

        for j in range(1,4):
            print(tic_tac.get((i,j)),end='')

            if j<3:
                print('|',end='')

            else:
                print('\n',end='')

        if i<3:
            print('-----')

    diagonalx = ((tic_tac.get((1,1))==tic_tac.get((2,2))==tic_tac.get((3,3))=='x'),
                 (tic_tac.get((3,3))==tic_tac.get((2,2))==tic_tac.get((1,1))=='x'))
    
    diagonalo = ((tic_tac.get((1,1))==tic_tac.get((2,2))==tic_tac.get((3,3))=='o'),
                 (tic_tac.get((3,3))==tic_tac.get((2,2))==tic_tac.get((1,1))=='o'))


    rowx = (tic_tac.get((1,1))==tic_tac.get((1,2))==tic_tac.get((1,3))=='x',
            tic_tac.get((2,1))==tic_tac.get((2,2))==tic_tac.get((2,3))=='x',
            tic_tac.get((3,1))==tic_tac.get((3,2))==tic_tac.get((3,3))=='x'
            )

    colo = (tic_tac.get((1,1))==tic_tac.get((2,1))==tic_tac.get((3,1))=='o',
            tic_tac.get((1,2))==tic_tac.get((2,2))==tic_tac.get((3,2))=='o',
            tic_tac.get((1,3))==tic_tac.get((2,3))==tic_tac.get((3,3))=='o'
            )

    rowo = (tic_tac.get((1,1))==tic_tac.get((1,2))==tic_tac.get((1,3))=='o',
            tic_tac.get((2,1))==tic_tac.get((2,2))==tic_tac.get((2,3))=='o',
            tic_tac.get((3,1))==tic_tac.get((3,2))==tic_tac.get((3,3))=='o'
            )

    colx = (tic_tac.get((1,1))==tic_tac.get((2,1))==tic_tac.get((3,1))=='x',
            tic_tac.get((1,2))==tic_tac.get((2,2))==tic_tac.get((3,2))=='x',
            tic_tac.get((1,3))==tic_tac.get((2,3))==tic_tac.get((3,3))=='x '
            )
    if any(rowo):
        print('player_2 won by horizontally')
        break

    elif any(rowx):
        print('player_1 won by horizontally')
        break

    elif any(colo):
        print('player_2 won by vertically')
        break

    elif any(colx):
        print('player_1 won by vertically')
        break

    elif any(diagonalo):
        print('player_2 won by diagonally')
        break

    elif any(diagonalx):
        print('player_1 won by diagonally')
        break
    
    elif len(m)==9:
        print('Tie')
        break

    else:
        continue
