from os import getcwd

full_path = getcwd()

if not "lesson" in full_path:
    full_path = full_path + "/lesson_11"

input_file = full_path + "/preproinsulin-seq.txt"

with open(input_file) as file:
    main_data = file.read()

def write_file(file_name, data, full_path):
    print(f"{file_name} length is {len(data)}")
    f = open(full_path + file_name, "w")
    f.write(data)
    f.close()

# Manually or programmatically delete ORIGIN, 1, 61, //, and the spaces and return carriages.
data = main_data
data = data.replace("ORIGIN", "")
data = data.replace("61", "")
data = data.replace("1", "")
data = data.replace("//", "")
data = data.replace(" ", "")
data = data.replace("\n", "")

# Save the file as preproinsulin-seq-clean.txt.
output_file = "/preproinsulin-seq-clean.txt"

# In the file preproinsulin-seq-clean.txt, copy your results.
write_file(output_file, data, full_path)

# Confirm that your file has 110 characters of lowercase letters, which represent the amino acids in the sequence of human preproinsulin.
print(f"Length of main data: {len(main_data)}")
print(f"Length of data.....: {len(data)}")

print(data)

# In lsinsulin-seq-clean.txt, save amino acids 1–24. Verify that your file has 24 characters.
write_file("/lsinsulin-seq-clean.txt", data[0:24], full_path)

# In binsulin-seq-clean.txt, save amino acids 25–54. Verify that your file has 30 characters.
write_file("/binsulin-seq-clean.txt", data[24:54], full_path)

# In cinsulin-seq-clean.txt, save amino acids 55–89. Verify that your file has 35 characters.
write_file("/cinsulin-seq-clean.txt", data[54:89], full_path)

# In ainsulin-seq-clean.txt, save amino acids 90–110. Verify that your file has 21 characters.
write_file("/ainsulin-seq-clean.txt", data[89:110], full_path)
