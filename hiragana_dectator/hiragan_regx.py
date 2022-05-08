# import re

# pattern = '/[あ-ん]+/u'
# text = input()
# x = re.search(text, pattern)
# print(x)

import re


string = input()
pattern = re.compile("[あ-ん]+")

if pattern.fullmatch(string) is not None:
    print("Found match: " + string)
else:
    print("No match")