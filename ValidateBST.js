# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def validate(self, root, min=None, max=None):
        return
    
    def isValidBST(self, root: TreeNode,min=None, max=None) -> bool:
        #print(root.val)
        if root==None:
            return True
        if(max!=None and root.val>=max):
            return False
        if(min!=None and root.val<=min):
            return False
        if(root.left and not self.isValidBST(root.left,min,root.val)):
            return False
        if(root.right and not self.isValidBST(root.right,root.val,max)):
            return False
        return True
