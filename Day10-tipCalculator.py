print('Tip Calculator')
spend = float(input('How much did you spend? '))
tip = int(input('What percentage do you want to tip? '))
people = int(input('How many people in your group? '))

total_tip = spend * (tip / 100)
total_bill = spend + total_tip
answer = total_bill / people

print(f'Each person should pay: ${round(answer, 2)}')
