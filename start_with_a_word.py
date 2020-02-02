import re

txt = "hello world"

#Check if the string starts with 'hello':

f = re.findall("^hello", txt)

if f:
  print(f)
else:
  print("No match")

