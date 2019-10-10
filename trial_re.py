import re

s = 'MMMCMXCIVCMCC'

spacial = re.findall('IV|IX|XL|XC|CD|CM', s)
rest = re.sub('IV|IX|XL|XC|CD|CM', '', s)
rest = [c for c in rest]
s = rest + spacial

print(spacial, rest)
