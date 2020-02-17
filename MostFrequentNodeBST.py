# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

If a tree has more than one mode, you can return them in any order.
                1
                \
                 2
                /
               2
    Ouput: [2]
    Maximum repeated element
'''
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        from collections import Counter
        
        res=[]
        if root==None:
            return []
        def inorder(node):
            if node.left!=None:
                inorder(node.left)
            res.append(node.val)
            if node.right!=None:
                inorder(node.right)
        inorder(root)
        count=Counter(res)
        print(count)
        res=[]
        maxcount=0
        maxele=0
        for key,val in count.items():
            if maxcount<val:
                maxele=key
                maxcount=val
        
        for key,val in count.items():
            if maxcount==val:
                res.append(key)
        return res
            
