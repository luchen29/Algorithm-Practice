class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        left = 0
        right = len(s)-1
        while left<right:
            if not s[left].isalpha() or s[left].isdigit():
                left += 1 
            if not s[right].isalpha() or s[right].isdigit():
                right -= 1 
            if s[left].lower() != s[right].lower():
                break
            else: 
                left += 1
                right -= 1
        if left >= right:
            return True
        return self.isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1)
        
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left].lower() != s[right].lower():
                return False
            else: 
                left += 1 
                right -= 1
        return True
        
