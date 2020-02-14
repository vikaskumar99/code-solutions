# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
'''
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        arr=[]
        if root==None:
            return []
        arr=[root,'s']
        temp=[]
        res=[]
        res=[[root.val]]
        while len(arr)>1:
            node=arr[0]
            if node=='s':
                res.append(temp)
                temp=[]
                arr.append('s')
            else:
                if node.left!=None:
                    arr.append(node.left)
                    temp.append(node.left.val)
                if node.right!=None:
                    arr.append(node.right)
                    temp.append(node.right.val)
                
                
            arr=arr[1:]
        print(res)
        maxrow=[]
        for temp in res:
            maxrow.append(max(temp))
        return maxrow
