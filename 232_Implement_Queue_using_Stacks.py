class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.listA = []
        self.listB = []
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        return self.listA.append(x)
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek()
        return self.listB.pop()
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while not self.listB:
            while self.listA:
                element = self.listA.pop()
                self.listB.append(element)
        return self.listB[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.listA == [] and self.listB == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()