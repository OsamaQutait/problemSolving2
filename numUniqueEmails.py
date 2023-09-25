from typing import *
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        h = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.replace(".", "")
            local = local.split("+")[0]
            email = local + "@" + domain
            h.add(email)
        return len(h)


if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    solution = Solution()
    print(solution.numUniqueEmails(emails))