print('Exam Grade Calculator')
exam = input('Name of exam: ')
total_score = 100
obtain_score = int(input('Your Score: '))
score = int(obtain_score / total_score * 100)
if(score >= 90 and score <= 100):
  print(f'Your Score: {score}%')
  print('A+')
elif(score >= 80 and score <= 90):
  print(f'Your Score: {score}%')
  print('A-')
elif(score >= 70 and score <= 80):
  print(f'Your Score: {score}%')
  print('B')
elif(score >= 60 and score <= 70):
  print(f'Your Score: {score}%')
  print('C')
elif(score >= 50 and score <= 60):
  print(f'Your Score: {score}%')
  print('D')
elif(score >= 40 and score <= 50):
  print(f'Your Score: {score}%')
  print('U')
else:
  print('Are you sure to obtain marks to pass the exam?')
