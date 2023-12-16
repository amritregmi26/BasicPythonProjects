class Solution:
    def first_repeated_char(self, s: str) -> str:
        hashmap = {}
        s = s.lower()
        for c in s:
            if c in list(hashmap.keys()) and c != " ":
                hashmap[c] += 1
            else: 
                hashmap[c] = 1
            if hashmap[c] == 2:
                return c     
        return "No repeating char"