class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return ""
        start = 0
        end = len(A)-1
        while start+1<end:
            mid = (start+end)//2
            if A[mid] < A[mid+1]:
                start = mid
            if A[mid] > A[mid+1]:
                end = mid
        if A[start] > A[end]:
            return start
        return end

# Binary Search
