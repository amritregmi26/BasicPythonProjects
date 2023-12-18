# Leetcode problem no. 929

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_email = set()

        for email in emails:
            i, local = 0, ""
            while(email[i] not in ["@", "+"]):
                if email[i] != ".":
                    local += email[i]
                i += 1
           
            while(email[i] != "@"):
               i += 1
            domain = email[i + 1:]
            unique_email.add(local + "@" + domain)
        return len(unique_email)