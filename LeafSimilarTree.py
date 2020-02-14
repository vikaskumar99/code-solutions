# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
                3
             /      \
            5         1
        /       \   /   \
        6       2   9   8
              /   \
             7     4

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
'''
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf1=leaf2=[]
        leaf=[]
        if root1==None or root2==None:
            return False
        def helper(root):
            if root.left==None and root.right==None:
                leaf.append(root.val)
                return
            if root.left!=None:
                helper(root.left)
            if root.right!=None:
                helper(root.right)
        helper(root1)
        leaf1=leaf
        leaf=[]
        helper(root2)
        leaf2=leaf
        
        if leaf1==leaf2:
            return True
        return False
