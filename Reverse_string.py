'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        low=0
        high=len(s)-1
        while(low<=high):
            swap=s[low]
            s[low]=s[high]
            s[high]=swap
            low+=1
            high-=1
        
        
