# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆
is_leap_year = False
# Write your code below this line 👇
if year % 4 == 0:
    is_leap_year = True
    if year % 100 == 0:
        is_leap_year = False
        if year % 400 == 0:
            is_leap_year = True
if is_leap_year:
  print("Leap year")
else:
  print("Not leap year")
