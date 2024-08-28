low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Please press ENTER to start")

guesses = 1
while low != high:
    print("\tCurrent guessing range is {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input(
        f"My guess is {guess}.  Should I guess (h)igher or (l)ower or (c)orrect? "
    )

    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print(f"I got it in {guesses}!")
        break
    else:
        print("Please enter h, l, or c")

    guesses += 1
else: 
    print(f"You thought of the number {low}")
    print(f"I got it in {guesses} guesses.")