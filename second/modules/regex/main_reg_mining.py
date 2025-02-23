##########################################################################################
# identifiers
#   Character	    Description	            Example Pattern Code	    Exammple Match
#   \d	            A digit	                file_\d\d	                file_25
#   \w	            Alphanumeric	        \w-\w\w\w	                A-b_1
#   \s	            White space	            a\sb\sc	                    a b c
#   \D	            A non digit	            \D\D\D	                    ABC
#   \W	            Non-alphanumeric	    \W\W\W\W\W	                *-+=)
#   \S	            Non-whitespace	        \S\S\S\S	                Yoyo

##########################################################################################
# quantifiers
#   Character	    Description	                    Example Pattern Code	    Exammple Match
#   +	            Occurs one or more times	    Version \w-\w+	            Version A-b1_1
#   {3}	            Occurs exactly 3 times	        \D{3}	                    abc
#   {2,4}	        Occurs 2 to 4 times	            \d{2,4}	                    123
#   {3,}	        Occurs 3 or more	            \w{3,}	                    anycharacters
#   \*	            Occurs zero or more times	    A\*B\*C*	                AAACC
#   ?	            Once or none	                plurals?	                plural

##########################################################################################
# additional operators
#  |    ->      or
#  .    ->      wildcard
#  ^    ->      starts with
#  $    ->      ends with
#  []   ->      exclude

##########################################################################################

import re

text = "My phone number is 408-555-1234"

matcher_1 = re.search(r"\d\d\d-\d\d\d-\d\d\d\d", text)
print(matcher_1.span())
print(matcher_1.group())

matcher_2 = re.search(r"\d{3}-\d{3}-\d{4}", text)
print(matcher_2.span())
print(matcher_2.group())

pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")  # groups multiple regex together, () is indicator for new regex
matcher_3 = re.search(pattern, text)
print(matcher_3.span())
print(matcher_3.group())
print(matcher_3.group(1))
print(matcher_3.group(2))
print(matcher_3.group(3))

matcher_4 = re.search(r"cat|dor", "the cat is here")
print(matcher_4.span())

matcher_5 = re.findall(r".at", "the cat in the hat sat here")
print(matcher_5)

matcher_6 = re.findall(r"^\d", "1 i am")
print(matcher_6)
matcher_7 = re.findall(r"^\d", "asd1 i am")
print(matcher_7)
matcher_8 = re.findall(r"^\d", "a 1 i am")
print(matcher_8)

matcher_9 = re.findall(r"\d$", "a 1 i am")
print(matcher_9)
matcher_10 = re.findall(r"\d$", "a 1 i am2")
print(matcher_10)

matcher_11 = re.findall(r"[^\d]+", "there ar12e 3 numbers 34 inside 5 this sequence")
print(matcher_11)
matcher_12 = re.findall(r"[^\W ]+", "sdjh! sadf,,. asdf. §§$%")
print(" ".join(matcher_12))

matcher_13 = re.findall(r"[\w]+-[\w]+", "asd asd af-asae sdf awe-asd asd")
print(matcher_13)

matcher_14 = re.findall(r"cat(aa|bb|cc)", "asd cataa, dkjfi catbb, ölaki slkd catcc")
print(matcher_14)
