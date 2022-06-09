"""
script to get list from a text file 
without any separator
"""

def texttolist(filename: str) -> list:
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

print(texttolist("text.txt")
# output - ["a","b","c"]
