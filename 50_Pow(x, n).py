class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x    
        if n < 0:
            x = 1/x
        power = self.myPow(x, abs(n)//2)
        power = power * power
        if n % 2 == 1:
            power = power * x
        return power

# pay attention to the condition: n<0.
# Use recursion n--> n//2. Time complexity: o(log(n))