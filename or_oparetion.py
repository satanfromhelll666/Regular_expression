import re

txt = "The rain in ai ai a Spain falls mainly in the plain!"

x = re.findall("in|ai", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
  
