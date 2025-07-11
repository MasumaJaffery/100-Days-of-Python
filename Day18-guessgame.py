print('One-Million-To-One')
guess_score = 5000
count = 0
while True:
  number = int(input('What is your guess?:'))
  if (guess_score == number):
    count += 1
    print('Correct')
    print(f'It took you {count} tries to get it correct!')
    break
  elif guess_score > number:
    count += 1
    print('Too low')
  elif guess_score < number:
    count += 1
    print('Too high')
  else:
    print('Try Again')
