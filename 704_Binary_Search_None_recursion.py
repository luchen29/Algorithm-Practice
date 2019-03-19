class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # None recursion method
        if not nums:
            return -1
        start = 0
        end = len(nums)-1
        while(start <= end):
            middle = int((start+end)/2)
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                start = middle+1
                continue
            if nums[middle] > target:
                end = middle-1
                continue
        return -1

# None Recursion method for binary search.
