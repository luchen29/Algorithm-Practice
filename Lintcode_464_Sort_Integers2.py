class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
    	start = 0
    	end = len(A)-1
    	self.quickSort(A, start, end)

    def quickSort(self, A, start, end):
    	if start >= end:
    		return 
    	left, right = start, end
    	pivot = A[(left+right)//2] 
    	while left <= right:
	    	while left<=right and A[left] < pivot:
	    		left += 1 
	    	while left<=right and A[right] > pivot:
	    		right -= 1 
	    	if left <= right:
	    		A[left], A[right] = A[right], A[left]
	    		left += 1 
	    		right -= 1 
	    self.quickSort(A, start, right)
	    self.quickSort(A, left, end)
