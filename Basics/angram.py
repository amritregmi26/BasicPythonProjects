class Solution: 
    def is_anagram(self, str1: str, str2: str) -> bool:
            return sorted(str1.lower()) == sorted(str2.lower())