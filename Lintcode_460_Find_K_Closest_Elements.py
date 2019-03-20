class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):
        if k == 0:
            return []
        n = len(A)
        result = []
        right = self.findClosestUpperIndex(A, target)
        left = right-1
        for _ in range(k):
            if self.is_left_closer(A, left, right, target):
                result.append(A[left])
                left -= 1
            else:
                result.append(A[right])
                right += 1
        return result

    def findClosestUpperIndex(self, A, target):
        start, end = 0, len(A) - 1
        while start+1<end:
            middle = (start+end)//2
            # if A[middle] = target:
            #     return middle
            if A[middle] >= target:
                end = middle
            else:
                start = middle
        if A[start]>= target:
            return start
        if A[end] >= target:
            return end
        return end+1


    def is_left_closer(self, A, left, right, target):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target
