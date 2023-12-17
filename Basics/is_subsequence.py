class Solution:
    def is_subsequence(self, str: str, seq: str) -> bool:
        i = j = 0
        while(i < len(seq) and j < len(str)):
            if(str[j] == seq[i]):
                i += 1
            j += 1
        return i == len(seq)