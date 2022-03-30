# Adding
from unicodedata import name


class Task():
    def __init__(self, query, result, name):
        self.query = query
        self.result = result
        self.name = name
        print(f"{self.name}\n{self.query} = {self.result}\n")

task01 = Task("2 + 2", 2 + 2, "Adding",)
task02 = Task("4 - 2", 4 - 2, "Substracting",)
task03 = Task("2 * 2", 2 * 2, "Multiplying")
task04 = Task("4 / 2", 4 / 2, "Dividing")
