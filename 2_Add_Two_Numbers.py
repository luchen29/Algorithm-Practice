# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carryPrev, carry, total = 0, 0, 0
        dummy = ListNode(0)
        tail = dummy
        while l1 or l2 or carryPrev != 0:
            if not l1 and not l2:
                curNode = ListNode(1)
                tail.next = curNode
                return dummy.next
            if l1 and not l2:
                total = l1.val + carryPrev
                l1 = l1.next
            elif l2 and not l1:
                total = l2.val + carryPrev
                l2 = l2.next
            else:
                total = l1.val + l2.val + carryPrev
                l1, l2 = l1.next, l2.next
            if total > 9:
                total = total % 10
                carry = 1
            else: carry = 0
            curNode = ListNode(total)
            tail.next = curNode
            tail = curNode
            carryPrev = carry
        return dummy.next
            
            

        