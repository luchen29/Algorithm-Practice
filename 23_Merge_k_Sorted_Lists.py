# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        while len(lists) > 1:
            newlists = []
            for n in range (0, len(lists), 2):
                if n+1 < len(lists):
                    newlist = self.mergeTwoLists(lists[n], lists[n+1])
                else: 
                    newlist = lists[n]
                newlists.append(newlist)
            lists =  newlists
        return lists[0]
        
    def mergeTwoLists(self, listA, listB):
        dummy = ListNode(None)
        tail = dummy
        while listA and listB: 
            if listA.val < listB.val:
                tail.next = listA
                listA = listA.next
            else: 
                tail.next = listB
                listB = listB.next
            tail = tail.next
        if listA: 
            tail.next = listA
        else: 
            tail.next = listB
        return dummy.next
        