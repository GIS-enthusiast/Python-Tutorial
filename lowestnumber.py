

import re
 
# Filters out everything but digits, minuses, pluses, and periods (for decimals)
PATTERN = re.compile('[^0-9\/\-\*\+\. ]')
 
def sanitize(string):
    # replace unicode u'\u2013' with ascii minus so python can eval as code
    string = string.replace('\u2013', '-')
    string = string.replace('X', '*')
    return PATTERN.sub('', string)
    
 
def calculateNumbers(lines):
    sanitizedLines = list(map(sanitize, lines))
    #print(sanitizedLines)
    evaluatedLines = list(map(eval, sanitizedLines))
    return evaluatedLines
    
    lowestNumber = min(evaluatedLines)
    for line, evaluation in zip(lines, evaluatedLines):
        print('{} = {}{}'.format(line, evaluation,
              (' (lowest)' if evaluation == lowestNumber else '')))
    


# '×'.encode('unicode-escape')

lines = ['2/3 + 15/6 wrong', '7/5 – 9/3', '17/8 X 20/4 correct', '12/5 – 20/7', '28/12 – 20/4']
string1 = '2/3 + 15/6 wrong'
print(string1)
print(PATTERN)
print(PATTERN.sub('!', string1))

    
#test = calculateNumbers(lines)
#print(test)
#print(type(lines))


'''
"""
Lets you paste in a series of arithmetic
expressions, evaluates them (line by line),
and tells you which one is the lowest.
 
Example input/output:
 
paste in the numbers and hit enter twice
2/3 – 15/6 wrong
7/5 – 9/3
17/8 – 20/4 correct
12/5 – 20/7
28/12 – 20/4
 
2/3 - 15/6  = -1.8333333333333335
7/5 - 9/3 = -1.6
17/8 - 20/4  = -2.875 (lowest)
12/5 - 20/7 = -0.4571428571428573
28/12 - 20/4 = -2.6666666666666665
"""
 
import re
 
# Filters out everything but digits, minuses, pluses, and periods (for decimals)
PATTERN = re.compile('[^0-9\/\-\+\*\. ]')
 
def sanitize(string):
    # replace unicode u'\u2013' with ascii minus so python can eval as code
    string = string.replace('\u2013', '-')
    string = string.replace('\u2212', '-')
    string = string.replace('\xd7', '*')
    return PATTERN.sub('', string)
 
 
def calculateNumbers(lines):
    sanitizedLines = list(map(sanitize, lines))
    evaluatedLines = list(map(eval, sanitizedLines))
    lowestNumber = min(evaluatedLines)
    for line, evaluation in zip(lines, evaluatedLines):
        print('{} = {}{}'.format(line, evaluation,
              (' (lowest)' if evaluation == lowestNumber else '')))
 
def main():
    while True:
        print("paste in the numbers and hit enter twice")
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        if lines:
            calculateNumbers(lines)
 
if __name__ == '__main__':
    main()
'''



