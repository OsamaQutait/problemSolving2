from typing import *
import re
def numUniqueEmails(emails: List[str]) -> int:
    email_sent = {str}
    for email in emails:
        index = email.rfind('@')
        match = (re.search('\\+', email))
        if match == None:
            email = email[:index].replace('.', '') + email[index:]
            email_sent.add(email)
            continue
        else:
            match = match.start()
        email = email[:match] + email[index:]
        index = email.rfind('@')
        email = email[:index].replace('.', '') + email[index:]
        email_sent.add(email)
    return len(email_sent)-1

if __name__ == '__main__':
    print(numUniqueEmails(
        ["test.email+alex@leetcode.com", "test.email@leetcode.com"]))
