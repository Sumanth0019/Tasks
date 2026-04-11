import re

emails = """
sumanth@gmail.com
sumanth123@yahoo.com
student-email@
"""

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}"

valid_emails = re.findall(pattern, emails)

print(valid_emails)