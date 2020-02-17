# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Given a complete binary tree, count the number of nodes.
Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        nodes=0
        res=[]
        if root==None:
            return 0
        def node(root):
            res.append(root)
            if root.left!=None:
                node(root.left)
            if root.right!=None:
                node(root.right)
        node(root)
        print(len(res))
        return len(res)
