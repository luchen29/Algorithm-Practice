class MinStack(object):

    def __init__(self):
        self.listA, self.min = [], []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.listA.append(x)
        if not self.min or x <= self.min[-1]:
            self.min.append(x)
            
    def pop(self):
        """
        :rtype: None
        """
        if self.listA[-1] == self.min[-1]:
            self.min.pop()
        return self.listA.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.listA[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()