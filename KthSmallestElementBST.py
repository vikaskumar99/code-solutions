# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
'''
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res=[]
        
        def inorder(node):
            if node.left!=None:
                inorder(node.left)
            res.append(node.val)
            if node.right!=None:
                inorder(node.right)
        inorder(root)
        print(res)
        
        return res[k-1]
