print('Fill in the blank Lyrics!')
print("(type in the blank lyrics, see if you're as cool as me)")
attempts = 0
while True:
    guess = input("Never going to ___ you up: ").lower()
    attempts += 1
    if guess == 'put':
        print("Nope, try again.")
    elif guess == 'let':
        print("Nope, try again.")
    elif guess == 'give':
        print("Well done, it only took you", attempts, "attempt(s)!")
        break
    else:
        print("Nope, try again.")
