class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s:
           return ""
        nn = len(s)
        if nn == 1:
            return s
        largest = 1
        largest_i = 0
        largest_j = 0
        dp5 = [[1]*nn for _ in range(nn)]
        for j in range(1,nn):
            for i in reversed(range(0,j)):
                if s[i] == s[j] and (dp5[i+1][j-1]==(j-i-1) if (j>=i+2) else True):
                    dp5[i][j] = 2 + dp5[i+1][j-1] if (j>=i+2) else 2
                    if dp5[i][j] > largest:
                        largest = dp5[i][j]
                        largest_i = i
                        largest_j = j
        return s[(largest_i):(largest_j+1)]

  # substring
  # Given a string S, find the longest palindromic substring in S.
  # You may assume that the maximum length of S is 1000, and there exists one
  # unique longest palindromic substring.
