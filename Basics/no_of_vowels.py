# Find the total no of vowels in a string

class Solution:
    def count_vowel(self, s: str) -> int:
        count = 0
        for c in s:
            c = c.lower()
            if(c == "a" or c == "e" or c == "i" or c == "o" or c == "u"):
                count += 1
        return count