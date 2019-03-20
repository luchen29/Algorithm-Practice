class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        lastElement = nums[len(nums)-1]
        firstIndex = self.findMinIndex(nums, lastElement)
        if target <= lastElement:
            start = firstIndex
            end = len(nums)-1 
            targetIndex = self.searchTarget(nums, start, end, target)
            return targetIndex 
        else:
            end = firstIndex
            start = 0
            targetIndex = self.searchTarget(nums, start, end, target)
            return targetIndex
    
    def findMinIndex(self, nums, lastElement):
        start = 0
        end = len(nums)-1 
        while start+1<end:
            mid = (start+end)//2
            if nums[mid] <= lastElement:
                end = mid 
            else:
                start = mid
        if nums[start] <= lastElement:
            return start
        return end
    
    def searchTarget(self, nums, start, end, target):
        while start+1<end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid 
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            return start 
        if nums[end] == target:
            return end 
        return -1
# two times of binary search, first: draw a line; second: search target.