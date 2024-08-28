available_parts = [
    "computer",
    "monitor",
    "keyboard",
    "mouse",
    "mouse pad",
    "hdmi cable",
]
current_choice = 99
computer_parts = []

while current_choice != "0":
    if 1 <= current_choice <= len(available_parts) + 1:
        part_name = available_parts[current_choice - 1]
        computer_parts.append(part_name)
        print(f"Added {part_name}.")
    elif current_choice == 0:
        print("Done shopping.")
        if len(computer_parts) > 0:
            print(computer_parts)
        else:
            print("No items in cart.")
        break
    else:
        for i, part_name in enumerate(available_parts):
            part_name = available_parts[i]
            print(f"{i + 1}.\t{part_name}")
        print("0.\tExit")
    current_choice = int(input())
