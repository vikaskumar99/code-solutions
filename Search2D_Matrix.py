'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=j=0
        low=high=mid=0
        if len(matrix)==0 or len(matrix[0])==0:
            print('entering')
            return False
        if len(matrix[0])==1 and target==matrix[0][0]:
            return True
        print(len(matrix))
        while(i<len(matrix)):
            if matrix[i][0]<=target and matrix[i][len(matrix[i])-1]>=target:
                low=0
                high=len(matrix[i])
                while(low<=high):
                    mid=(low+high)//2
                    
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid]<target:
                        low=mid+1
                    else:
                        high=mid-1   
                return False
            else:
                i+=1
        return False
        
