
### random expression

"""
import re

pattern = r"eggs"

if re.match(pattern,"pallavieggspallavi"):
    print("match found")
else:
    print("match not found")

if re.search(pattern,"pallavieggseggspallavieggs"):
    print("match found")
else:
    print("match not found")

if re.findall(pattern,"pallavieggspallavi"):
    print("match found")
else:
    print("match not found")

print(re.findall(pattern,"pallavieggseggspallavieggs"))
# print(re.search(pattern,"pallavieggspallavi"))

"""

### find and replace
"""
import re

string = "my name is pallavi,pallavi is good girl"

pattern = r"pallavi"

newstring = (re.sub(pattern , "Sonali", string))
print(newstring)

"""

### dot metacharacter:
"""
import re

pattern = r"app...e"

if re.match(pattern,"appnlsejfhf"):
    print("match found")
"""

### CARET AND DOLAR METACHARACTER (^, $) :

"""
import re

pattern = "^gr.y$"

if re.match(pattern,"greyy"):
    print("match found")

"""

### CHARACTER CLASS :

"""
import re

pattern = r"[a-z][a-z][0-9]"

if re.search(pattern,"aa2"):
    print("match found")


# pattern = r"[a].[0-6]"
# 
# if re.search(pattern,"a2"):
#     print("match found")

"""

### STAR METACHARACTER :

"""
import re

pattern = r"eggs(bacon)*"

if re.match(pattern,"eggsbacon"):
    print("match found")

"""

### GROUP :

import re

pattern = r"eggs(bread)*boil"

if re.match(pattern, "eggsbreadboil"):
    print("match found")