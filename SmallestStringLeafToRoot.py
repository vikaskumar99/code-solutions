# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
Example 1:

https://assets.leetcode.com/uploads/2019/01/30/tree1.png

Input: [0,1,2,3,4,3,4]
Output: "dba"
'''
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        allpaths=[]
        if root==None:
            return ''
        from string import ascii_lowercase
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
        
        for i in range(len(allpaths)):
            allpaths[i].reverse()
            for j in range(len(allpaths[i])):
                allpaths[i][j]=ascii_lowercase[allpaths[i][j]]
            allpaths[i]=''.join(map(str,allpaths[i]))
        allpaths.sort()
        print(allpaths)
        return allpaths[0]
        
