# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

            1
              \
                3
               /
              2
    output : 1
'''
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res=[]
        
        def inorder(node):
            if node.left!=None:
                inorder(node.left)
            res.append(node.val)
            if node.right!=None:
                inorder(node.right)
        inorder(root)
        print(res)
        diff=999999
        for i in range(len(res)-1):
            if res[i+1]-res[i]<diff:
                diff=res[i+1]-res[i]
        print(diff)
        return diff
        
