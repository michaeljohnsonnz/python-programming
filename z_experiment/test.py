import json

with open("test.json") as json_file:
    data = json.load(json_file)

    print("Type: ", type(data))

    print(data["name"])