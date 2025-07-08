print('Rock-Paper-Scissors Game')
score1 = 0
score2 = 0

while True:
    Player1 = input('Player 1 (Rock, Paper, Scissors or Q to quit): ').strip().capitalize()
    if Player1 == 'Q':
        break

    Player2 = input('Player 2 (Rock, Paper, Scissors or Q to quit): ').strip().capitalize()
    if Player2 == 'Q':
        break

    if Player1 == Player2:
        print('Tie Result')
        continue

    # Rock vs Paper
    if Player1 == 'Rock' and Player2 == 'Paper':
        score2 += 1
        print("Player2's Paper smothers Player1's Rock!")
    elif Player1 == 'Paper' and Player2 == 'Rock':
        score1 += 1
        print("Player1's Paper smothers Player2's Rock!")

    # Scissors vs Paper
    elif Player1 == 'Scissors' and Player2 == 'Paper':
        score1 += 1
        print("Player1's Scissors chops Player2's Paper!")
    elif Player1 == 'Paper' and Player2 == 'Scissors':
        score2 += 1
        print("Player2's Scissors chops Player1's Paper!")

    # Rock vs Scissors
    elif Player1 == 'Rock' and Player2 == 'Scissors':
        score1 += 1
        print("Player1's Rock crushes Player2's Scissors!")
    elif Player1 == 'Scissors' and Player2 == 'Rock':
        score2 += 1
        print("Player2's Rock crushes Player1's Scissors!")

    else:
        print("Invalid input! Please type Rock, Paper, or Scissors.")

    # Check win condition
    if score1 == 2:
        print('🏆 Player1 wins with 2 victories!')
        break
    elif score2 == 2:
        print('🏆 Player2 wins with 2 victories!')
        break
