"""

https://leetcode.com/problems/powx-n/submissions/
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
"""

def brute_force(x, n):
    num = abs(n)
    ans = 1.0
    while(num > 0):
        ans = ans * x
        num -= 1
    if n < 0:
        ans = 1.0 / ans
    return ans

def better_solution(x, n):
    ans = 1.0
    num = abs(n)

    while num > 0:
        #print("line", ans, x, num)
        if num % 2 == 1:
            ans = ans * x
        x = x * x
        num = num // 2

    if n < 0:
        ans = 1.0 / ans

    return ans


x = 2
n = -10
print(better_solution(x, n),  pow(x, n))
print(brute_force(x, n))
