
# In-place rotate
class Solution(object):
    def rotate(self, nums, k):
        if not nums:
            return 
        length = len(nums)
        k = k % length
        nums[:k], nums[k:length] = nums[length-k:length], nums[:length-k]


# No need for in-place:
class Solution:
    def rotate(self, nums, k):
        if not nums:
            return 
        length = len(nums)
        k = k % length
        result = nums[length-k:length] + nums[:length-k]
        return result