# Task 1: The Selective DJ
# Loop through a slice of the genres list from the previous question and print out the genres. 
# Use slicing to create a sublist of genres from the second to the fourth track.

tracks = ["Track 1", "Track 2", "Track 3", "Track 4", "Track 5" ]
track_list = tracks[1:4]

for track in track_list:
    print("Sublist of " + track)


user_input = input("Next Task")

# Task 2: The One-Liner Band with List Comprehensions
# Use a list comprehension to create a new list that contains each genre with the word "Music" appended to it. 
# Print this new list.

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for genre in genres:
    print(f"{genre}, Music")


user_input = input("Last one")
# Task 3: Numerical Beats with range
# Write a loop using range() to print out a countdown from 10 to 1, followed by the message "The beat drops now!".

count_down = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

for i in range(len(count_down)):
    print(f"{count_down[i]} The Beat drops now!")