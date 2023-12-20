class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split(" ")
        reversed_s = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] != "":
                reversed_s += f"{s[i].strip()} "
        return reversed_s.strip()