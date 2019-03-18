class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1

        for i in xrange(0, len(haystack)-len(needle)+1):
            j = 0
            while j < len(needle):
                if haystack[i+j] != needle[j]:
                    break
                else: j += 1
            if j == len(needle):
                return i
        return -1

# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
