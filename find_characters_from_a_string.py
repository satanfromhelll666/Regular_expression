import re

txt = "The rain in ai ai a Spain falls mainly in the plain! 1"

x = re.findall("[tai]", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

