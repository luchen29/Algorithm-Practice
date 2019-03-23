# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None 
        fast = head 
        slow = head 
        while fast.next is not None:
            fast = fast.next.next
            slow = slow.next 
            if fast is None and slow is not None:
                return slow 
        return slow

# Fast node: 2 step/ time
# Slow node: 2 step/ time
# when fast reach the end, slow is in the middle.