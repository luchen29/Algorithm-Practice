class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not g or not s:
            return 0
        g = sorted(g)
        s = sorted(s)
        i, j, count = 0, 0, 0
        while i<len(s) and j<len(g):
            if g[j] <= s[i]:
                count += 1
                j += 1
            i += 1
        return count
            
   