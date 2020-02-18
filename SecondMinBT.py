# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
'''
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res=[]
        if root==None:
            return -1
        def inorder(node):
            if node.left!=None:
                inorder(node.left)
            res.append(node.val)
            if node.right!=None:
                inorder(node.right)
        inorder(root)
        print(res)
        
        res=list(set(res))
        res.sort()
        if len(res)>1:
            return res[1]
        return -1
        
