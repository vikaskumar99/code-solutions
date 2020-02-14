# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        arr=[]
        if root==None:
            return []
        arr=[root,'s']
        temp=[]
        res=[]
        res=[[root.val]]
        while len(arr)>1:
            node=arr[0]
            if node=='s':
                res.append(temp)
                temp=[]
                arr.append('s')
            else:
                if node.left!=None:
                    arr.append(node.left)
                    temp.append(node.left.val)
                if node.right!=None:
                    arr.append(node.right)
                    temp.append(node.right.val)
                
                
            arr=arr[1:]
        res.reverse()
        print(res)
        return res
