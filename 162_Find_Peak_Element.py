class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: 
            return -1 

        start = 0
        end = len(nums)-1 
        while start+1<end:
            mid = (start+end)//2 
            if nums[mid]>nums[mid-1] and nums[mid]<nums[mid+1]:
                start = mid
            elif nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid 
            else:
                end = mid
        if nums[start]>nums[end]:
            return start
        return end

# Four conditions when drawing the mid-line: it is peak; it is bottom; it's going up; it's going down.
