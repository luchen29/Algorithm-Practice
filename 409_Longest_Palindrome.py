class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = {}
        for c in s:
            if c in hash:
                del hash[c]
            else:
                hash[c]=True
        remove = len(hash)
        if remove >= 1:
            remove -= 1
        return len(s)-remove

# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Idea: hash table, find the odd num pairs and even num pairs.
