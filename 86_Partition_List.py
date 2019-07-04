# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummyLarge = ListNode(0)
        dummySmall = ListNode(0)
        dummyLarge.next, dummySmall.next = head, head
        p, q = dummyLarge, dummySmall        
        while head:
            temp = head.next
            if head.val >= x:
                p.next = head
                p = head
            else:
                q.next = head
                q = head
            head = temp
        p.next = None
        q.next = dummyLarge.next
        return dummySmall.next
        