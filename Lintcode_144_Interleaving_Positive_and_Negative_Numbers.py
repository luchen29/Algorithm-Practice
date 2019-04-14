class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        if len(A)<=1:
            return 
        left = 0
        right = len(A)-1
        # partitio: all negative leftside-all positive right-side
        while left <= right:
            while left<=right and A[left]<0:
                left += 1 
            while left<=right and A[right]>0:
                right -= 1 
            if left<=right:
                A[left],A[right] = A[right],A[left]
                left += 1 
                right -= 1 

        #get the positive and negative count
        negLength = len(A[:left])
        posiLength= len(A[left:])

        #makesure positive and negative counts meet needs. (abs<=1)
        if abs(posiLength-negLength)>1:
            return 
        #set left& right index according to different condition.
        left = 1 if negLength >= posiLength else 0
        right = len(A)-2 if posiLength >= negLength else len(A)-1
        
        #swipe value, each 2 nums.
        while left<right:
            A[left],A[right] = A[right],A[left]
            left += 2 
            right -= 2
        return A
    
        
