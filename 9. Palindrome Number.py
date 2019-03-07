class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        number = x
        y = 0
        i = 0
        while number > 0:
            i = number % 10
            y = y * 10 + i
            number = number // 10
                
        return x == y 
