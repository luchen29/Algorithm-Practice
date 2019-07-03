# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        mPointer, nPointer = head, head
        for i in range(1, m):
            mPointer = mPointer.next
        for j in range(1,n):
            nPointer = nPointer.next
        tempRight = nPointer.next
        prev, start = None, head
        posIdx = 1
        while head:
            if posIdx + 1 == m:
                temp = head.next
                head.next = nPointer
            elif posIdx == m:
                temp = head.next
                head.next = tempRight
            elif posIdx > m and posIdx <= n:
                temp = head.next
                head.next = prev
            else:
                temp = head.next
            head, prev = temp, head
            posIdx += 1    
        if m == 1:
            return nPointer
        else:
            return start
        