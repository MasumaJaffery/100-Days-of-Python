print('〽️')
name = input('What is your good name?')
if name.isalpha():
  # .isalpha() returns True only if all characters are letters (no digits, no spaces).
  print('Hola Amigo', name)
# .isdigit() returns True only if all characters are digits).
elif name.isdigit():
  print('Hola Robot', name)
else:
  print('Hola!')
