# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''
class Solution:
    def hasPathSum(self, root: TreeNode, sums: int) -> bool:
        allpaths=[]
        path=[]
        haspath=False
        def paths(node,path,allpaths):
            if node==None:
                return
            path.append(node.val)
            
            if node.left==None and node.right==None:
                allpaths.append(path)
            
            paths(node.left,path[:],allpaths)
            paths(node.right,path[:],allpaths)
        
        paths(root,[],allpaths)
        print(allpaths)
        
        for temp in allpaths:
            if sum(temp)==sums:
                return True
        return False
        