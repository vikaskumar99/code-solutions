# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        allpaths=[]
        path=[]
        
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
        
        maxlen=0
        for temp in allpaths:
            if len(temp)>maxlen:
                maxlen=len(temp)
        return maxlen
