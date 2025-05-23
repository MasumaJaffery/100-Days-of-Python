print('Rock-Paper-Scissors Game')

Player1 = input('Player 1 :').strip().capitalize()
Player2 = input('Player 2 :').strip().capitalize()
Rock = 'R'
Paper = 'P'
Scissors = 'Scissors' 
if (Player1 == Player2):
  print('Match Draw')
elif (Player1 == Paper and Player2 == Rock):
  print('Player 1 Wins!')
elif (Player1 == Rock and Player2 == Paper):
  print('Player 2 Wins!')
elif (Player1 == Rock and Player2 == Scissors):
  print('Player 1 Wins!')
elif (Player1 == Scissors and Player2 == Rock):
  print('Player 2 Wins!')
elif (Player1 == Scissors and Player2 == Paper):
  print('Player 1 Wins!')
elif (Player1 == Paper and Player2 == Scissors):
  print('Player 2 Wins!')
else:
  print('Different Choice!')
