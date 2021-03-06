'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i=0
        found=False
        if len(nums)==0:
            return [-1,-1]
        if len(nums)==1 and target!=nums[0]:
            return [-1,-1]
        elif len(nums)==1 and target==nums[0]:
            return [0,0]

        for i in range(len(nums)):
            if nums[i]==target:
                found=True
                break
        if found==False:
            return [-1,-1]
        start=i
        print('start',start)
        while i<len(nums) and nums[i]==target:
            i+=1
        end=i-1
        
        return [start,end]
