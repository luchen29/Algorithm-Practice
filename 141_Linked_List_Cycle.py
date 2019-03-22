# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        nodeA, nodeB = head, head
        while True:
            if nodeA.next is not None:
                nodeA = nodeA.next.next
                nodeB = nodeB.next
                if nodeA is None or nodeB is None:
                    return False
                if nodeA is nodeB:
                    return True
            else:
                return False
        return False

# Pay attention to the logic.                
                
                
        