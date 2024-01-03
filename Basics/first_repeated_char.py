class Solution:
    def first_repeated_char(self, s: str) -> str:
        hashmap = {}
        for c in s:
            c = c.lower()
            
            if c not in hashmap and c.isalnum():
                hashmap[c] = 1
                
            elif c in hashmap: 
                hashmap[c] += 1
                
                if hashmap[c] > 1:
                    return c
            
        return "No character is repeated"