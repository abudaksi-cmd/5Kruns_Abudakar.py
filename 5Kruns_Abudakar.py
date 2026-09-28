# 5K Runs Mini Project
# Sophia Abudakar

# Set starting values
total_minutes = 0
number_of_runs = 0

# Ask the user for the first 5K run time
run_time = input("Enter minutes for a 5K run (press Enter when finished): ")

# Continue asking for run times until the user presses Enter
while run_time != "":
    run_time = int(run_time)
    total_minutes = total_minutes + run_time
    number_of_runs = number_of_runs + 1

    run_time = input("Enter minutes for another 5K run (press Enter when finished): ")

# Calculate the averages
average_run = total_minutes / number_of_runs
average_kilometer = average_run / 5

# Display the results
print("Number of runs:", number_of_runs)
print("Total minutes:", total_minutes)
print("Average minutes per 5K run:", round(average_run, 2))
print("Average minutes per kilometer:", round(average_kilometer, 2))
