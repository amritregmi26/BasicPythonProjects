class Solution:
    def is_palindrome(self, str: str) -> bool:
        reversed = ""
        for i in range(len(str) - 1, -1, -1):
            reversed += str[i]
        return reversed == str
