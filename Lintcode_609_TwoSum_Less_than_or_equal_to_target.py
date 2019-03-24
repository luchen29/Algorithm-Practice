class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        if len(nums)<=1:
            return 0 
        nums.sort()
        left = 0
        right = len(nums)-1 
        count = 0
        while left < right:
            # if left > 0 and nums[left] == nums[left-1]:
            #     left += 1 
            #     continue
            if nums[left] + nums[right] > target:
                right -= 1 
            else:
                count = count + (right-left) 
                left += 1 
        return count
               