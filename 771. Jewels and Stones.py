class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        x = 0
        for i in S:
            if i in J:
                x += 1
        return x
