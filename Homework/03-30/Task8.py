#Write a Python program that reads a JSON file containing a list of dictionaries, sorts the list by a specific key, 
#and writes the sorted list back to the file.

import json

key = "name"
with open("People.json", "r") as f:
    people = json.load(f)["people"]
    
people.sort(key=lambda person:person[key])

with open("People.json","w") as f:
    json.dump({"people":people},f)
