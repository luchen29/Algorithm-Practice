class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """
    def enqueue(self, item):
        # write your code here
        if self.dummy.next is None:
            self.dummy.next = ListNode(item)
            self.tail = self.dummy.next
        else:
            self.tail.next = ListNode(item)
            self.tail = self.tail.next
    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        if self.dummy.next is None:
            return None
        head = self.dummy.next
        self.dummy.next = head.next
        return head.val
    
    def __init__(self):
        self.dummy, self.tail = ListNode(None), ListNode(None)