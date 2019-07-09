class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 
        self.quickSort(nums, 0, len(nums)-1)
        return nums[-k]
    
    def quickSort(self, nums, start, end):
        if start >= end:
            return nums     
        left, right = start, end
        mid = nums[(start+end)//2]        
        while left <= right:
            while left <= right and nums[left] < mid:
                left += 1
            while left <= right and nums[right] > mid:
                right -= 1          
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)
    
    
        
            
        
        