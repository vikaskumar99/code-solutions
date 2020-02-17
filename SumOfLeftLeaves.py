# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        leftsum=0
        lefts=[]
        sums=0
        if root==None:
            return 0
        count=0
        def left(node,sums,side):
            if node.left==None and node.right==None and side==1:
                lefts.append(node.val)
                sums+=node.val
            if node.left!=None:
                
                left(node.left,sums,1)
            if node.right!=None:
                left(node.right,sums,0)
                
        left(root,sums,0)
        print(lefts)
        return sum(lefts)            
