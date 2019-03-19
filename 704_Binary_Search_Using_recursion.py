class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(nums,0,len(nums)-1,target)

    def binarySearch(self, nums, start, end, target):
        if start>end:
            return -1
        middle = int((start + end)/2)
        if nums[middle] == target:
            return middle
        if nums[middle]<target:
            return self.binarySearch(nums,middle+1,end,target)
        return self.binarySearch(nums,start,middle-1,target)


# Define recursive binary search function for solving the problem.
