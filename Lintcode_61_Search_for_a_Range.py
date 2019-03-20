class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        if A == []:
            return [-1,-1]
        result = []
        firstPos = self.searchFirstPos(A, target)
        result.append(firstPos)
        lastPos = self.searchLastPos(A, target)
        result.append(lastPos)
        return result
        
    def searchFirstPos(self, A, target):    
        start = 0 
        end = len(A)-1 
        while start+1<end:
            mid = (start+end)//2 
            if A[mid] >= target:
                end = mid
            else: 
                start =  mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end 
        return -1
    
    def searchLastPos(self, A, target):
        start = 0 
        end = len(A)-1 
        while start+1<end:
            mid = (start+end)//2 
            if A[mid] > target:
                end = mid
            else: 
                start =  mid
        if A[end] == target:
            return end
        if A[start] == target:
            return start 
        return -1
        