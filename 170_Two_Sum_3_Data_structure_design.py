class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.nums.append(number)
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        self.nums.sort()
        left = 0
        right = len(self.nums)-1
        while left < right:
            if self.nums[left] + self.nums[right] == value:
                return True
            elif self.nums[left] + self.nums[right] < value:
                left += 1 
            else: 
                right -= 1 
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)