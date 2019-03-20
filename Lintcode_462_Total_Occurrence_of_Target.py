class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        if A == []:
            return 0
        firstPos = self.findFirstPos(A, target)
        lastPos = self.findLastPos(A, target)
        if firstPos>=0 or lastPos>=0:
            occurrence = (lastPos-firstPos)+1
            return occurrence
        return 0
        
    def findFirstPos(self, A, target):
        start = 0
        end = len(A)-1
        while start+1<end:
            mid = (start+end)//2
            if A[mid] >= target:
                end = mid
            else: 
                start = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end 
        return -1
    
    def findLastPos(self, A, target):
        start = 0
        end = len(A)-1
        while start+1<end:
            mid = (start+end)//2
            if A[mid] > target:
                end = mid
            else: 
                start = mid
        if A[end] == target:
            return end 
        if A[start] == target:
            return start
        return -1

