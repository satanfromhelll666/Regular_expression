import re
txt = 'hello wo8ld'

x = re.findall('wo..d' ,txt )

print(x)

'''
output
wo8ld

'''
