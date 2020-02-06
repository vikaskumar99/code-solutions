# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
Share
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        i=0
        list1=ListNode(0)
        if head==None:
            return None
        list1.next=head
        fast=list1
        slow=list1
        temp=list1
        while(i<n and fast.next!=None):
            fast=fast.next
            i+=1
        while(fast.next!=None):
            entered=True
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        
        return list1.next
