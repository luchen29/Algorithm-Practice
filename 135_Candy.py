class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        if len(ratings) == 1:
            return 1
        
        candy = [1] * len(ratings)
        reverse = ratings[::-1]
        for i in range (1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        for i in range (1, len(reverse)):
            if reverse[i] > reverse[i-1] and candy[len(ratings)-i-1] < candy[len(ratings)-i] + 1:
                candy[len(ratings)-i-1] = candy[len(ratings)-i] + 1
        return sum(candy)