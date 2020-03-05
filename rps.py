print('...rock...')
print('...paper...')
print('...scissors...')

player_one = input('Input player 1\'s choice: ')
player_two = input('Input player 2\'s choice: ')

print('SHOOT!')

if player_one == player_two:
	print('DRAW! Play again.')
elif player_one == 'rock':
	if player_two == 'scissors':
		print('Player 1 wins')
	else:
		print('Player 2 wins')
elif player_one == 'scissors':
	if player_two == 'paper':
		print('Player 1 wins')
	else:
		print('Player 2 wins')
elif player_one == 'paper':
	if player_two == 'rock':
		print('Player 1 wins')
	else:
		print('Player 2 wins')
else: 
	print('You messed up the game somehow..')
