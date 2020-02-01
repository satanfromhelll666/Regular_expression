import re
txt = '123 and your will see 45 6'

x = re.findall('\d' ,txt )

print(x)

'''
output
['1', '2', '3', '4', '5', '6']
'''
