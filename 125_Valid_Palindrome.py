class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        i = 0
        j = len(s)-1
        while i<=j:
            if s[i].isalpha() or s[i].isdigit():
                s_i = s[i]
            else:
                i += 1
                continue
            if s[j].isalpha() or s[j].isdigit():
                s_j = s[j]
            else:
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True

# Given a string, determine if it is a palindrome, considering only alphanumeric
# characters and ignoring cases.
