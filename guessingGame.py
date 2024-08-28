import random

highest = 10
answer = random.randint(1, highest)
totalTries = 3
curGuess = 0
print(f"Please guess a number between 1 and {highest} in {totalTries} attempts.")
for i in range(totalTries):
    curGuess = int(input(f"Guess {i+1} of {totalTries}: "))
    if curGuess == answer:
        print(f"You got it in {i+1} tries!")
        break
    if curGuess < answer:
        print("Guess higher")
    else:
        print("Guess lower")
print("You were unable to guess the correct number: {}".format(answer))