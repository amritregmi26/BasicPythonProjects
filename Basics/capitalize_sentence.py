class Solution:
    def capitalize_sentence(self, sen: str) -> str:
        sen_arr = sen.strip().split(' ')
        capitalized = [word[0].upper() + word[1:] for word in sen_arr]
        return " ".join(capitalized)
