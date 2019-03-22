class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                if nums[left] != nums[right]:
                    nums[left] = nums[right]
                left += 1
            right += 1 
        for n in range(left, len(nums)):
            nums[n] = 0
        return nums

# Idea:
# two pointers: left is the current position needed to be deside; right is the position used as "copy source";
# Right: jump over if meet a 0; Stop if !=0
# when right != 0, check if left == right (queal means no need to change); if not equal, then overlap the original left-value by using the "copy source" (current right value).
# set all values after current left position to 0.