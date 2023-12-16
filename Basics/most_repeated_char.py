class Solution:
    def most_repeated_char(self, s: str) -> str:
        hashmap = {}
        s = s.lower()

        for c in s:
            if (c in list(hashmap.keys()) and c != " "):
               hashmap[c] += 1
            else:
                hashmap[c] = 1
        
        # error in sorting logic
        hashmap = dict(sorted(hashmap.items(), key= lambda item: item[1], reverse=True))

        return list(hashmap)[0][0]

print(Solution().most_repeated_char("testing 123 testing"))