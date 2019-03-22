"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """

    #Method 1:
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        nodeA, nodeB = headA, headB
        lenA, lenB = 1, 1
        while nodeA.next is not None:
            lenA += 1 
            nodeA = nodeA.next
        while nodeB.next is not None:
            lenB += 1 
            nodeB = nodeB.next 
                
        nodeA, nodeB = headA, headB
        while lenA>lenB:
            nodeA = nodeA.next
            lenA -= 1 
        while lenA<lenB:
            nodeB = nodeB.next
            lenB -= 1 
        while nodeA is not nodeB:
            nodeA = nodeA.next 
            nodeB = nodeB.next
        return nodeA

    #Method 2:
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        nodeA = headA
        nodeB = headB
        while nodeA is not nodeB:
            if nodeA.next is None and nodeB.next is None:
                return None
            if nodeA.next is None and nodeB.next is not None:
                nodeA = headB
                nodeB = nodeB.next
                continue
            if nodeB.next is None and nodeA.next is not None:
                nodeB = headA
                nodeA = nodeA.next
                continue
            nodeA = nodeA.next
            nodeB = nodeB.next
        return nodeA
    

# Two methods: 
# Method 1: get the length of both links; reduce the length of the longer one, and compare node.next togher to see if they're the same node --> the intersection node.
# Method 2: let the length of links be A+B and B+A; therefore they have the same length, and will convert at last. (also compare the node.nest to see if they're the same node--> "None")
