'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos=i=0
        
        while i<len(nums):
            if nums[i]!=0:
                nums[pos]=nums[i]
                pos+=1
            i+=1
        while pos<len(nums):
            nums[pos]=0
            pos+=1
        
        
        
        
