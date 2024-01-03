class Solution:
    def most_repeated_char(self, str1: str) -> str:
        hashmap ={}
        for s in str1:
            s = s.lower()
            if s not in hashmap and s.isalnum():
                hashmap[s] = 1
            elif s in hashmap:
                hashmap[s] += 1
        hashmap = sorted(hashmap.items(), key = lambda item: item[1], reverse=True)
        return hashmap[0][0]
  