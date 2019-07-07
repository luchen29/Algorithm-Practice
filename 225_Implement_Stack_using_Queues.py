class MyStack(object):
    def __init__(self):
        self.listA, self.listB = [], []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.listA:
            for i in range(0, len(self.listA)):
                self.listB.append(self.listA[i]) 
            while self.listA:
                self.listA.pop()
        self.listA.append(x)
        for i in range(0, len(self.listB)):
            self.listA.append(self.listB[i])
        while self.listB:
            self.listB.pop()        
    def pop(self):
        """
        :rtype: int
        """
        return self.listA.pop(0) 
    def top(self):
        """
        :rtype: int
        """
        return self.listA[0]
    def empty(self):
        """
        :rtype: bool
        """
        return self.listA == [] and self.listB == []
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()