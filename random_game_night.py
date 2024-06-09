# Task 1: Random Choice Game
# Create a game where a player has a list of items. They have to guess which item in the list was selected. 
# Use random.choice() to select the item and take the user's guess via input. 
# Provide feedback on whether they guessed correctly or not.

items = ["Book", "Glass", "Plate", "Key", "Pencil"]

import random

for i in range(len(items)):
    user_input = str(input("What item?"))
    if user_input == random.choice(items[i]):
        print(f"{random.choice(items[i])} You've guessed correctly")
else:
    print("You've guessed wrong")
        

