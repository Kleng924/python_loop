# Task 1: Loop Condition Exploration
# Write a while loop with a condition that will never be false (an infinite loop). 
# Inside the loop, print a statement. Then, use a break statement to exit the loop after 5 iterations.

color_of_the_sky = "blue"

counter = 0 
while color_of_the_sky != "green":
    print(color_of_the_sky) 
    counter += 1
    if counter == 5:
        break

user_input = input("Hi!")
# Task 2: Conditional Exit
# Modify the infinite loop from Task 1 to include a condition that will eventually be false and 
# remove the break statement. The loop should terminate naturally once the condition is met.

counter = 0 
while color_of_the_sky != "green":
    print(color_of_the_sky) 
    counter += 1
    if counter == 3:
        color_of_the_sky = "green"
    
