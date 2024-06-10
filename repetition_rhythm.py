# Task 1: The for Loop DJ Set
# Using the provided genres list, write a for loop that prints out each genre with a custom message. 
# Extend this task by adding a counter that displays the number of the track before the genre.

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
tracks = ["Track1", "Track2", "Track3", "Track4"]
messages = ["Smooth!", "Right On!", "To the Hop!", "Finest!"]

for i in range(len(genres)):
    genre = genres[i]
    track = tracks[i]
    message = messages[i]
    print(f"{track}:{genre},{message}")

user_input = input("Next")
# Task 2: The Remix Artist with while
# Convert the for loop from Task 1 into a while loop. 
# Ensure it performs the same function but also includes a condition to stop the loop if a 
# certain genre is played for instance Hip-hop.

while i in range(len(genres)):
    print(f"{track}:{genre},{message}")
    if genre == ['Hip-hop']:
       track == ["Track3"]
       message == ["To the Hop!"]
    break


user_input = input("Hi")
# Task 3: Light Show Technician Loop
# Using the range() function, loop through the genres list by index. 
# For each genre, print out the track number and a message that the light show is ready. 
# Modify the loop to skip a genre if it's not suitable for the light show, for instance Classical genre.


for i in range(len(genres)):
    genre = genres[i]
    track = tracks[i]
    message = messages[i]
    print(f"{genre}:, {track}:, + The light show is ready!")
