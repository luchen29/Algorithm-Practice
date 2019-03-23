class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        left = 0
        right = 0
        while left <= right and right <= len(nums)-1:
            if nums[right] != nums[left]:
                nums[left+1] = nums[right]
                left += 1
            else: 
                right += 1        
        return left+1
        
        
        