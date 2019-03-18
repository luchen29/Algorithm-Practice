class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        if source is None or target is None:
            return -1
        n = len(source)
        m = len(target)
        if m==0:
            return 0

        base = 10 ** 6
        targetCode = 0
        for i in range(0,m):
            targetCode = (targetCode * 31 + ord(target[i])) % base

        hashCode = 0
        for i in range(0, n):
            # abc+d
            hashCode = (hashCode * 31 + ord(source[i])) % base
            if i < m: continue
            # abcd-a
            hashCode = hashCode - (ord(source[i-m])*((31**m) %base)) %base
            if hashCode < 0:
                hashCode = hashCode + base
            #compare if targetCode == HashCode
            if hashCode == targetCode:
                if source[i-m+1:i] == target[0:m-1]:
                    return (i-m+1)
        return -1

# Lintcode 594: strStr II
# Rabin Karp Algorithm--> use Harsh code to represent sting, reduce the inner
# cycle time form o(n) to 1.
