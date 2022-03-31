from re import search
from os import getcwd

GREEN  = '\033[22;32;49m'
RESET  = '\033[00m'

full_path = getcwd()

if not "lesson" in full_path:
    full_path = full_path + "/lesson_11"

input_file = full_path + "/preproinsulin-seq-original.txt"

with open(input_file) as file:
    data = file.read()

start_of_data = search(r'ORIGIN(.+)', data)
end_of_data = search(r"//", data)

range_start = start_of_data.span()[0]
range_end = end_of_data.span()[1]

result = data[range_start:range_end]

output_file = full_path + "/preproinsulin-seq.txt"

write_file = open(output_file, "w")
write_file.write(result)
write_file.close()

print(f"Successfully created {GREEN}{output_file}{RESET}")