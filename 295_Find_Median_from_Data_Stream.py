import heapq
class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap, self.minheap = [], []
        self.mediam = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.maxheap) <= len(self.minheap):
            heapq.heappush(self.maxheap, -num)
        else: heapq.heappush(self.minheap, num)
        if len(self.maxheap) == 0 or len(self.minheap) == 0:
            self.mediam = []
            self.mediam.append(-self.maxheap[0])
            return
        if -self.maxheap[0] > self.minheap[0]:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        self.mediam = []
        if len(self.maxheap) == len(self.minheap):
            self.mediam.append(-self.maxheap[0])
            self.mediam.append(self.minheap[0])
        else:
            self.mediam.append(-self.maxheap[0])

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.mediam)%2 == 1:
            return float(self.mediam[0])
        return float(self.mediam[0]+self.mediam[1])/2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()