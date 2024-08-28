colors = ["Red", "Blue", "Green", "Purple"]

print("Please choose from the list below:")
num_items = len(colors)

choice = 99

while choice != 0:
    if 1 <= choice <= num_items:
        print(f"You chose option {choice}")
    else:
        for i in range(num_items):
            print(f"{i+1}.\t{colors[i]}")
        print("0.\tExit")

    choice = int(input())
else:
    print("Program terminated.")