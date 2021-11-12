m=[] 

n=1

tic_tac={(1,1):'-',
		(1,2):'-',
		(1,3):'-',
		(2,1):'-',
		(2,2):'-',
		(2,3):'-',
		(3,1):'-',
		(3,2):'-',
		(3,3):'-'}



while True:
	c = True
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
		print("!!position out of range.!!")
                
		c = False
	
	else:
		pass
		
	for i in m:
		if i==(a,b):
			print('values_repeated')
			quit()
			break
			
		else:
			pass
			
	if c==True:
		m.append((a,b))
	
	else:
		pass

	for i in range(1,4):
		for j in range(1,4):
			print(tic_tac.get((i,j)),end='')
			if j<3:
				print('|',end='')

			else:
				print('\n',end='')

		if i<3:
			print('-----')
			
		else:
			pass

	diagonalx = ((tic_tac.get((1,1))==tic_tac.get((2,2))==tic_tac.get((3,3))=='x'),
				(tic_tac.get((3,1))==tic_tac.get((2,2))==tic_tac.get((1,3))=='x')
				)

	diagonalo = ((tic_tac.get((1,1))==tic_tac.get((2,2))==tic_tac.get((3,3))=='o'),
				(tic_tac.get((3,1))==tic_tac.get((2,2))==tic_tac.get((1,3))=='o')
				)


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
		print('Player 2 won by horizontally')
		break

	elif any(rowx):
		print('Player 1 won by horizontally')
		break

	elif any(colo):
		print('Player 2 won by vertically')
		break

	elif any(colx):
		print('Player 1 won by vertically')
		break

	elif any(diagonalo):
		print('Player 2 won by diagonally')
		break

	elif any(diagonalx):
		print('Player 1 won by diagonally')
		break

	elif len(m)==9:
		print('Tie')
		break

	else:
		continue
