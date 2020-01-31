'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows

'''

class Solution:
    def reverse(self, x: int) -> int:
        strnum=str(x)
        negflag=0
        
        if strnum[0]=='-':
            negflag=1
            strnum=strnum[1:]
        strnum=''.join(reversed(list(strnum)))
        print(strnum)
        if negflag==1:
           strnum='-'+strnum
        reversenum=int(strnum)
        if reversenum>(-2**31) and reversenum<((2**31) -1):
            return reversenum
        else:
            return 0
        
