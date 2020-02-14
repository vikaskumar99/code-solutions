# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2     
     / \   
    1   3
'''
class Solution:

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if root==None:
            return None
        if root.val==val:
            print('equal')
            print('root',root)
            return root
        elif val<root.val:
            print('left')
            return self.searchBST(root.left,val)
        else:
            print('right')
            return self.searchBST(root.right,val)
