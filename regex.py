#71200553
#stefanus emmanuel lefrand wuisang


import re

values = [ ("M", 1000), ("D", 500), ("C", 100),
    ("L", 50), ("X", 10), ("V", 5), ("I", 1) ]

def romanNumeralToInt(romanNum):
    for (c, v) in values:
        match = re.match("(.?)(" + c + "+)(.)", romanNum)   
        if match:                                          
            return len(match.group(2)) * v \
                - romanNumeralToInt(match.group(1)) \
                + romanNumeralToInt(match.group(3))
    return 0

a=str(input())
v=a.upper()
print(romanNumeralToInt(v))

