print('Generation Identifer')
dob = int(input('Which year you were born?'));
if (1883 <= dob <= 1990):
  print('Lost Generation')
elif (1901 <= dob <= 1927):
  print('Greatest Generation')
elif (1928 <= dob <= 1945):
  print('Silent Generation')
elif(1946 <= dob <= 1964):
  print('Baby Boomers')
elif(1965 <= dob <= 1980):
  print('Generation X')
elif(1981 <= dob <= 1996):
  print('Millennials')
elif(1997 <= dob <= 2012):
  print('Generation Z')
elif(2013 <= dob <= 2024):
  print('Generation Alpha')
elif(2025 <= dob <= 2035):
  print('Generation Beta')
else:
  print('Try Again!')