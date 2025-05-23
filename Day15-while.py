exit = 'yes'
while exit.lower() != 'no':
    animal = input('Which animal you want? : ')
    if animal.lower() == 'cow':
        print('A Cow goes moo');
    else:
        print('Umm... the Lesser Spotted Lemur goes Awooga?')
    exit = input('Do you want to exit? (yes/no): ')