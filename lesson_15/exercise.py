import os
import subprocess

# Exercise 1: Using os.system
os.system("ls -la")

# Exercise 2: Using subprocess.run
subprocess.run(["ls"])

# Exercise 3: Using subprocess.run with two arguments
subprocess.run(["ls", "-la"])

# Exercise 4: Using subprocess.run with three arguments
subprocess.run(["ls", "-la", "README.md"])

# Exercise 5: Retrieving system information
command1 = "uname"
commandArgument1 = "-a"
print(f"Gathering system information with command: {command1} {commandArgument1}")
subprocess.run([command1, commandArgument1])

# Exercise 6: Retrieving information about disk space
command2 = "ps"
commandArgument2 = "-x"
print(f"Gathering active process information with command: {command2} {commandArgument2}")
subprocess.run([command2, commandArgument2])