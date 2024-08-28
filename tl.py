print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")  # What is your name?
name2 = input("What is their name? ")  # What is their name?

combined_name = name1 + name2
combined_name = combined_name.upper()
score = 0

score += combined_name.count("T")
score += combined_name.count("R")
score += combined_name.count("U")
score += combined_name.count("E")
true_score = score
score = 0
score += combined_name.count("L")
score += combined_name.count("O")
score += combined_name.count("V")
score += combined_name.count("E")
love_score = score
total_score = int(f"{true_score}{love_score}")
if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
