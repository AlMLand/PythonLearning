import re

text = "The agent's phone number is 408-555-1234. Call soon, phone is waiting!"

#####
matcher_1 = re.search("phone", text)
if matcher_1:
    print(matcher_1.start())  # shows start index
    print(matcher_1.end())  # shows end index
    print(matcher_1.span())  # shows the start and end indices

#####
matcher_2 = re.findall("phone", text)
if len(matcher_2) != 0:
    print(matcher_2)

#####
matcher_3 = re.finditer("phone", text)
for match in matcher_3:
    print(match.group())
