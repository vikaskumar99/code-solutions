"""

Given a number 123, print the next largest number. i.e 213
213 -> 231
321 -> 123 (back to smallest)

"""


"""
Brute Force: 

Find all the permutations of the string

Then find the min positive diff between the permutations and the string. That will be the answer
If no min_diff then the string is the largest number possible, return the reversed string

"""

def brute_force(string):
    import itertools
    combinations = list(itertools.permutations(string, len(string)))
    #print(combinations)
    num = int(string)
    all_combo = []

    for item in combinations:
        temp = int("".join(item))
        all_combo.append(temp)

    #print(all_combo)
    min_diff = 9999999999999999999999
    next_ele = 0

    for item in all_combo:
        diff = item - num
        if diff > 0:
            #print("enter if", diff, item, min_diff)
            if diff < min_diff:
                print(num, item, diff, min_diff)
                next_ele = item
                min_diff = diff
    if not next_ele:
        return "".join(reversed(string))

    return next_ele

def better_solution(nums):
    nums = list(nums)
    i = len(nums) - 1
    while (i > 0):
        if nums[i - 1] < nums[i]:
            break
        i -= 1

    if i == 0:
        nums.reverse()
        return "".join(nums)
    i -= 1

    j = len(nums) - 1
    while (j > 0):
        if nums[i] < nums[j]:
            break
        j -= 1

    nums[i], nums[j] = nums[j], nums[i]

    left = i + 1
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return "".join(nums)

string = "15432"
print("Input", string)
print("Answer is = ", brute_force(string))
print("Answer is = ", better_solution(string))

