
# Quick sort: 
# Time: O(nlog(n));
# Space: O(1)
def sortIntegers2(self, A):
	self.quickSort(A, 0, len(A)-1)

def quickSort(self, A, start, end):
	left, right = start, end
	midIndex = (left+right)//2 
	midValue = A[midIndex]
	while left <= right:
		while left <= right and A[left] < midValue:
			left += 1 
		while left <= right and A[right] > midValue:
			right -= 1 
		if left <= right:
			A[left], A[right] = A[right], A[left]
			left += 1 
			right -= 1 
	self.quickSort(A, start, right)
	self.quickSort(A, left, eng)




