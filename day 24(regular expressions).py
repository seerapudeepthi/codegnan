Regular Expression (RegEx)
--------------------------

-->RegEx is a sequence of char that form a searching pattern...
-->This can be used to check if a string contian the specified search pattern
-->Python has a built-in package called 're' which can be used to work with RegEx

FUNCTIONS in re
---------------
1.Findall
2.Search
3.Fullmatch
[]-->a-z,A-Z,0-9 and any specified squence
.-->Here each dot is one char
^-->This look for the, string is starting with specified squence or not...
$-->This look for the, string is ending with specified squence or not
*-->Zero or more
?-->Zero or one
+-->One or more

SPECIAL SEQUENCE
---------------
"""\\S-->no space
\\s--> only space
\\D--> non - digits
\\d--> only-digits
\\w--> matchs any word char(letters,digits,underscore)
\\W--> non - words..
"""


import re
any1 = "RegEx is a sequence of char that form a searching pattern"
print(re.findall('[e]', any1))
print(re.search('[e]', any1))
print(re.fullmatch('[e]', any1))

any = "Python has a built-in package called 're' which can be 678 used to work with RegEx"
print(re.findall('[a-zA-Z]', any))
print(re.findall('[lcs]', any))
print(re.findall('[0-10]', any))
print(re.search('[hs]', any))
print(re.fullmatch('[e]', any))
print(re.findall('^Python has',any))
print(re.findall('pac..........d', any))
print(re.findall('RegEx$', any))
print(re.findall('ca.*led', any))
print(re.findall('P.{20}', any))
print(re.findall('pac.+n', any))
print(re.findall('called.*', any))
print(re.findall(r'\D+', any))
print(re.findall(r'\d+', any))
print(re.findall(r'\S+', any))
print(re.findall(r'\s+', any))
print(re.findall(r'\w+', any))
print(re.findall(r'\W+', any))

mobile = input("Enter 10 digit mobile number:")
how = re.fullmatch('[6-9][0-9]{9}',mobile)
if how:
    print(f"{mobile} is india number")
else:
    print(f"{mobile} is not india number")
