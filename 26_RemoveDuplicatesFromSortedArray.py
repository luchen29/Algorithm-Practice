# requirements: in-place, no extra memory
# double pointer: left+1(the first duplicate pos); right(the first new pos)
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        left,right = 0, 0
        while left <= right and right <= len(nums)-1:
            if nums[left] != nums[right]:
                nums[left+1] = nums[right]
                left += 1 
            else:
                right += 1 
        return left+1



