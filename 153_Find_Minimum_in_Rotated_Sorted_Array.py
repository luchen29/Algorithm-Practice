class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end = len(nums)-1
        end_value = nums[end]
        return self.findFirstSmaller(nums, end_value)

    def findFirstSmaller(self, nums, target):
        start = 0
        end = len(nums)-1
        while start+1<end:
            mid = (start+end)//2
            if nums[mid] < target:
                end = mid
            if nums[mid] > target:
                start = mid
        if nums[start] <= target:
            return nums[start]
        if nums[end] <= target:
            return nums[end]

# Binary search OOXX.
# Decide a threshold, use binary search method to search for the first smaller one.
