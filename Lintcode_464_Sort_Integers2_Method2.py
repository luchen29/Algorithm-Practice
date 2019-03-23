# Merge Sort:
# Time: O(nlog(n))
# Space: O(n)
def sortIntegers2(self, A):
    if A is None or A==[]:
        return 
    n = len(A)
    temp = [0]*n
    start = 0
    end = n - 1 
    self.mergeSort(A, start, end, temp)

    
def mergeSort(self, A, start, end, temp):
    if start >= end:
        return
    mid = (start + end)//2 
    self.mergeSort(A, start, mid, temp)
    self.mergeSort(A, mid+1, end, temp)
    self.merge(A, start, end, temp)

def merge(self, A, start, end, temp):
    mid = (start+end)//2
    left = start
    right = mid+1
    tempIndex = left
    while left <= mid and right <= end:
        if A[left] < A[right]:
            temp[tempIndex] = A[left]
            left += 1 
            tempIndex += 1 
        else: 
            temp[tempIndex] = A[right]
            right += 1 
            tempIndex += 1 
    while left > mid and right <= end:
        temp[tempIndex] = A[right]
        right += 1 
        tempIndex += 1 
    while right > end and left <= mid:
        temp[tempIndex] = A[left]
        left += 1 
        tempIndex += 1 
    for i in range(start, end+1):
        A[i] = temp[i]