"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head and head.next:
            temp = head.next.next
            prev.next = head.next
            head.next.next = head 
            head.next = temp
            prev = head
            head = head.next
        return dummy.next
