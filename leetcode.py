import re
import pandas as pd

s = 'abc + 123'
s2 = '    -42'

PATTERN = re.compile('[^0-9\-\+]')
PATTERN2 = re.compile('[\-\+!^0-9]')

s = re.sub(r"^\s+", "", s)


print(s)
# put string sequences into list
list1 = []
list1[:0] = s
print(list1)

if PATTERN2.search(list1[0]) == None:
    print(int(0))

else:
    string = PATTERN.sub('', s)
    print(string)
