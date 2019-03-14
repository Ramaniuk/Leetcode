class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        high = n
        low = 1
        middle = 0        
        while guess (middle) != 0:
            middle = (high - low) / 2 + low  
            if guess (middle) == 0:
                return middle             
            elif guess (middle) == 1:
                low = middle + 1
            elif guess (middle) == -1:
                high = middle - 1   
