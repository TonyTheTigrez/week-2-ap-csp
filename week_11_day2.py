# open up the vscode from previous day
# create a new file called: week11_day1.py
# ----------------------------------------
# Day 2 Review Activity: My Personal Info Generator
# ----------------------------------------

print(" Welcome to the Python Review Activity!")
print("You’ll review variables, strings, numbers, and print formatting.\n")

# Step 1: Create Variables
# TODO: Replace the values below with your own info
first_name = "Anthony"
age = 30
favorite_color = "Blue"
favorite_number = 7
number4 = 4

#  Step 2: Practice String Operations
# 1. Print your name in uppercase
print(first_name.upper())

# 2. Print how many letters are in your name
print(len(first_name))

# 3. Combine your name and favorite color into one message
print(f"My name is {first_name} and my favorite color is {favorite_color}")

#  Step 3: Math Practice
# Use arithmetic operators with your favorite number
fav3 = int(favorite_number) + int(number4)
print(f"My favorite number plus 3 is {fav3}  ")
#  Step 4: User Input Practice
# Ask the user two questions and combine answers
number1 = int(input("What is your favorite number?: "))
number2 = int(input("What is your second fav number?: "))
number3 = number1 + number2
print(f"Your favorite number plus your second favorite number is {number3}")


# ⚙️ Step 5: Final Challenge (combine it all)
# Use math and strings together
fav_word = input("What is your fav word?: ")
fav_word2 = input("What is your second fav word?: ")
numberofletters = int(len(fav_word)) + int(len(fav_word2))
print(f"The length of both of your favorite words combined is {numberofletters}")
