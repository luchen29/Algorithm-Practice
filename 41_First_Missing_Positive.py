class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """     
        if not nums:
            return 1 
        for i in range(0,len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
        for i in range(0,len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return nums[-1] + 1

# The idea is to fine the first missing positive number.
# 每一位index上都应该对应相应的数 即num[i] == i+1 
# 进行swap交换，随后找到第一个不对应的
                