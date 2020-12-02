import re

pattern = re.compile(r"[a-zA-Z0-9#%$@]{8,}\d")

password = 'gegwedss$#%5'

a = pattern.fullmatch(password)

print(a)

# conditions were min 8 charactors
# can contain #%$@
# must end with a number
