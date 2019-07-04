"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None
        
        nodeA, nodeB, nodeC = head, head, head
        while nodeA:
            temp = nodeA.next 
            copyNode = RandomListNode(nodeA.label)
            nodeA.next = copyNode
            copyNode.next = temp
            nodeA = temp
            
        while nodeB and nodeB.next:
            temp = nodeB.next.next
            copyRandom = nodeB.random
            nodeB.next.random = copyRandom
            nodeB = temp
        
        dummy = RandomListNode(0)
        dummy.next = nodeC
        pointer = dummy
        while nodeC and nodeC.next:
            temp = nodeC.next.next
            pointer.next = nodeC.next
            pointer = nodeC.next
            nodeC = temp
        return dummy.next