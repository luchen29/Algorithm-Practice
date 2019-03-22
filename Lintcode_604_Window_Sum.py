class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        if nums==[] or k > len(nums):
            return []
        left = 0
        right = (left+k)-1
        sumNum = 0
        sumArray = []
        for i in range(left, right+1):
            sumNum += nums[i]
        sumArray.append(sumNum)
        if k == len(nums):
            return sumArray
        
        while right < len(nums)-1:
            right += 1
            sumNum = sumNum - nums[left] + nums[right]
            sumArray.append(sumNum)
            left += 1
        return sumArray

# calculate the sum of first k numbers, then add-in the next right and substracte the previous left.       
    
    
