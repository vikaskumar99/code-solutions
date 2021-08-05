

"""
Brute Force:

Loop through the whole array and check if string[:i] * length(string)/string[:i] = string
"""

def brute_force(string):
    for i in range(1, len(string)//2 + 1):
        if string[:i] * (len(string) // len(string[:i])) == string:
            return string[:i]

"""
Better solution:

If the string is repeating, then you will find the string in (string+string).

If found return the [0:found_idx]
Else, return None
"""

def better_solution(string):
    idx = (string+string).find(string, 1, -1)
    if idx == -1:
        return None
    return string[:idx]

string = "111111"
print(brute_force(string))
print(better_solution(string))