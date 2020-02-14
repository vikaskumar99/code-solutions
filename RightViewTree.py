# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        arr=[]
        if root==None:
            return []
        arr=[root,'s']
        temp=[]
        res=[]
        res2=[]
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
        print(res)
        for temp in res:
            res2.append(temp[-1])
        return res2
        
