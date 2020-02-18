# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
'''
class Solution:
    '''val=0
    def sums(self,node,val,left,right):
        if node==None:
            return
        
        if node.val>=left and node.val<=right:
            self.val+=node.val
        self.sums(node.left,val,left,right)
        self.sums(node.right,val,left,right)
    
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root==None:
            return 0
        self.sums(root,0,L,R)
        print(self.val)
        return self.val
      ''' 
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res=[]
        val=0
        def inorder(node):
            if node.left!=None:
                inorder(node.left)
            res.append(node.val)
            if node.right!=None:
                inorder(node.right)
        inorder(root)
        for i in res:
            if i>=L and i<=R:
                val+=i
        print(val)
        return val
