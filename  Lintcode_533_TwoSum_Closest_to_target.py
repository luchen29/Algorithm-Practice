class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        if len(nums)<=1:
            return None 
        nums.sort()
        left = 0
        right = len(nums)-1
        diff = abs((nums[left]+nums[right])-target)
        while left < right:
            if left > 0 and nums[left]==nums[left-1]:
                left += 1 
                continue
            if nums[left] + nums[right] > target:
                diff = min(diff, abs((nums[left] + nums[right])-target))
                right -= 1 
            else: 
                diff = min(diff, abs((nums[left] + nums[right])-target))
                left += 1 
        return diff
            
    
