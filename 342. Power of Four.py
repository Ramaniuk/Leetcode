class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        i = 1
        while i < num:
            i = i * 4
        return i == num
