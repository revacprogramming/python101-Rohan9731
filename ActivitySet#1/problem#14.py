# Using Web Services
# https://www.py4e.com/lessons/servces
  
   #working
import re
fh = open("regex_sum_269097.txt")
sum = 0
for line in fh:
   num = re.findall('[0-9]+',line)
   length = len(num)
   for i in range(length):
      sum += int(num[i])
print(sum)