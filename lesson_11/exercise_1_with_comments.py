# Bonus: Cleaning preproinsulin-seq.txt programmatically
# See lesson_11/README.md for more info about this bonus exercise
# I've used comments for learning purposes but I think the
# code I've written is self-explanatory

# Import just the function and not the whole library
from re import search
from os import getcwd

# For colorized output on the cli
GREEN  = '\033[22;32;49m'
RESET  = '\033[00m'

# Get current working directory
current_working_directory = getcwd()

# Add the lesson_11 directory to this path so this script can also be
# executed from the parent directory python-programming.
if not "lesson" in current_working_directory:
    full_path = current_working_directory + "/lesson_11/"

# Prepend the full path to the input file name 
input_file = full_path + "preproinsulin-seq-original.txt"

# Open file, read all its contents and store in variable
with open(input_file) as file:
    data = file.read()

# Find "ORIGIN" in the data
start_of_data = search(r'ORIGIN(.+)', data)

# Find "//" in the data
end_of_data = search(r"//", data)

# Get the range from span 
range_start = start_of_data.span()[0]
range_end = end_of_data.span()[1]

# Extract the data we need for this exercise
result = data[range_start:range_end]

# Prepend the full path to the output file name
output_file = full_path + "preproinsulin-seq.txt"

# Create a new file. write the result, and close file.
stream = open(output_file, "w")
stream.write(result)
stream.close()

# Let user know what's happening
print(f"Successfully created {GREEN}{output_file}{RESET}")