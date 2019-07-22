import json

f = open("survey.json", "r")
x = json.load(f)
print(len(x))
