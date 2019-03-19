class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        if not nums:
            return -1
        start = 0
        end = len(nums)-1
        while (start+1<end):
            middle = int((start+end)/2)
            if nums[middle] == target:
                end = middle
                continue
            if nums[middle] < target:
                start = middle + 1
                continue
            if nums[middle] > target:
                end = middle - 1
                continue
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
# Search for the first position of Target. Related to the classic binary search.
