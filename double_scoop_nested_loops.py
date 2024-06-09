# Task 1: Your Mood Tracker
# Simulate a mood tracker that records your mood at three different times of the day 
# (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: 
# the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. 
# For each time, randomly select a mood from a predefined list and print it.

# Example Outcome: An example would be "On Tuesday afternoon you were sad" 
# "On Tuesday night you were happy" "On Wednesday morning you were tired"

moods = ["happy", "sad", "energetic", "calm"]
times = ["morning", "afternoon", "evening"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

import random
for i in range(len(days)):
    print(f"On {days[i]} {random.choice(times)} you were {random.choice(moods)}")
