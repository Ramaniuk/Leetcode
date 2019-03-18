class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        new_s = ""
        new_string = ""                
        characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for char in s:
            if char in characters:
                new_s = new_s + char
                new_string = char + new_string
        print (s)
        print (new_s)
        print (new_string)

        return new_string == new_s
