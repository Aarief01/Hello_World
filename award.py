# Ask the participant how many minutes they took for each of the three events of the triathlon.
# Swimming:
# Cycling:
# Running:
# Calculate the participants total time by adding together the times of each event.
# Create a conditional statement to determine the awards based on the participants performance.
# If the participants total time is less than or equal to the 100 min:
# Print the participants total time and the award 'Provincial colours'.
# Elif the total time is less than or equal to 105 min:
# Print the participants total time and the award 'Provincial half colours'.
# Elif the total time is less than or equal to 110 mim:
# Else:
# Print the participants total time and 'No Award'.

# Request users input for their time in minutes for each of the triathlon events.
print("Please enter how many minutes you took for each of the triathlon events below:")
swimming = int(input("Swimming: "))
cycling = int(input("Cycling: "))
running = int(input("Running: "))

# Calculates the participants total time for the triathlon.
participants_total_time = swimming + cycling + running

award = True

# Create a conditional statement to determine the participants award based on their total time.
if participants_total_time <= 100:
    award = "Provincial Colours"
    print(f"Your time is {participants_total_time} minutes, you received {award}.")

elif participants_total_time <= 105:
    award = "Provincial Half Colours"
    print(f"Your time is {participants_total_time} minutes, you received {award}.")

elif participants_total_time <= 110:
    award = "Provincial Scroll"
    print(f"Your time is {participants_total_time} minutes, you received {award}.")

else:
    award = "no award"
    print(f"Your time is {participants_total_time} minutes, you received {award}.")
