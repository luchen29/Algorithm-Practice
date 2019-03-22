"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        if head is None:
            return None
        fast = head
        slow = head
        fast = self.findMeetPosition(fast,slow)
        if fast == -1:
            return None
        while fast is not slow:
            slow = slow.next
            fast = fast.next
        return fast
        
    def findMeetPosition(self,fast,slow):
        while True:
            if fast.next is not None:
                fast = fast.next.next
                slow = slow.next
                if fast is None or slow is None:
                    return -1
                if fast is slow:
                    return fast
            else:
                return -1
        return -1

# fast: a+b+c+b 
# slow: a+b
# Speed(fast) == 2 * Speed(slow) --> a+b+c+b == 2 * (a+b) --> a == c