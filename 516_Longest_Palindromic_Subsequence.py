class Solution(object):
    def longestPalindromeSubseq(self, s):
        if not s:
            return ""
        n = len(s)
        if n == 1:
            return 1
        dp = [[1]*n for _ in range(n)]
        for j in xrange (1, n):
            for i in reversed(xrange(0,j)):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1] if i+1<=j-1 else 2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[i][j]

# Description: Given a string s, find the longest palindromic subsequence's
# length in s. You may assume that the maximum length of s is 1000.

# Idea: DP, n*n list, dp[i][j] depends on: dp[i+1][j-1]// dp[i+1][j]// dp[i][j-1] 
