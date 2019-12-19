import re

s = 'aboutfucku'

spacial = re.findall('u', s)
rest = re.sub('fuck', '', s)
print(spacial)
print(rest)