'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums=list(set(nums))
        nums.sort()
        val=1
        print(nums)
        i=0
        if len(nums)==0:
            return 1
        for i in range(len(nums)):
            if nums[i]>0:
                print('vallll', i )
                break
        print(nums[i])
        #[-1,1,3,4]
        
        while  i<len(nums) and val==nums[i]:
            val+=1
            i+=1
            print('enter')
        return val
        
        
