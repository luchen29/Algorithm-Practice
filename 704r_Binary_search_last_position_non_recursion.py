class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        start = 0
        end = len(nums)-1
        while start+1 < end:
            middle = int((start+end)/2)
            if nums[middle] == target:
                start = middle
                continue
            if nums[middle] < target:
                start = middle + 1
                continue
            if nums[middle] > target:
                end = middle - 1
                continue
        if nums[end]==target:
            return end
        if nums[start]==target:
            return start
        return -1
        
# Search for the last position of Target. Related to the classic binary search.
