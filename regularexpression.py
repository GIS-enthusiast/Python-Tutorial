import re

# email validation copied from google and checked here: https://regex101.com/
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

string = 'b@b.com'

#print('search' in string)

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)  # true if completely identical
d = pattern.match(string)


print(a.span())  # shows where in string the search occurs
print(a.start())  # shows where it starts
print(a.group())  # returns matches
print(a.group(1))  # only prints results from group one (([a-zA-Z]))
