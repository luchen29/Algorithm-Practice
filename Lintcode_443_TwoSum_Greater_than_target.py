class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        if len(nums) <= 1:
            return 0
        nums.sort()
        left, right = 0, len(nums)-1
        count = 0
        while left < right:
            if nums[left]+nums[right] <= target:
                left += 1 
                continue
            else:
                count += right - left 
                right -= 1 
        return count
                
                
                
