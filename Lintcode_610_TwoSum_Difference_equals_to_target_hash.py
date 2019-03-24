class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        if len(nums)<=1:
            return None
        #key: nums[index] 
        #value: index
        hash = {}
        for i in range(0,len(nums)):
            if nums[i]+target in hash:
                return [hash[nums[i]+target]+1,i+1]
            if nums[i]-target in hash:
                return [hash[nums[i]-target]+1,i+1]
            hash[nums[i]] = i 
        return None   
            
# Key: nums[index]
# Value: index 
# Because need to return index+1.     
        
        
