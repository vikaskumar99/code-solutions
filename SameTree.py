# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
if root1==None and root2==None:
                return
            
            if root1.val!=root2.val:
                return False
            
            if((root1.left!=None and root2.left==None) or (root1.left==None and root2.left!=None)):
                return False
            else:
                return pretraverse(root1.left,root2.left)
            
            if((root1.right!=None and root2.right==None) or (root1.right==None and root2.right!=None)):
                return False
            else:
                return pretraverse(root1.right,root2.right)
        res=pretraverse(root1,root2)
        return res
'''

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        root1=p
        root2=q
        if p==None and q==None:
            return True
        def pretraverse(root1,root2):
            print('enter')
            if root1==None and root2==None:
                return
            if((root1 is None and root2 is not None) or (root1 is not None and root2 is None)):
                return False
            print('root1',root1.val)
            print('root2',root2.val)
            if root1.val!=root2.val:
                print('not equal')
                return False
            
            left=pretraverse(root1.left,root2.left)
            if left is False:
                return False
            
            right=pretraverse(root1.right, root2.right)
            if right is False:
                return False
        res=pretraverse(root1,root2)
        if res is None:
            return True
        
        return False
       
