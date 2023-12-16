# Problem Statement: Given a string of parantheses consisting () and {}, return number of paranthesis required to make the given string balanced.

class Solution:
    def no_of_parantheses(self, str: str) -> int:
        co = cc = so = sc = 0
        for char in str:
            match char:
                case '(':
                    so += 1
                    continue
                case ')':
                    sc += 1
                    continue
                case '{':
                    co += 1
                    continue
                case '}':
                    cc += 1
                    continue

        curly = co - cc if co > cc else cc - co
        small = so - sc if so > sc else sc - so

        return curly + small