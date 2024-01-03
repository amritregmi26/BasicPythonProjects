class Solution:
    def group_anagram(self, words: list[str]) -> list[str]:
        hashmap = {}
        for word in words:
            word = word.lower()
            key = "".join(sorted(word))
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)
        return list(hashmap.values())
