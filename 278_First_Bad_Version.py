# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start+1<end:
            middle = (start+end)//2
            if isBadVersion(middle):
                end = middle
            else:
                start = middle
        if isBadVersion(start):
            return start
        return end

# Binery search pattern: OOXX
# Related: first position of target number
