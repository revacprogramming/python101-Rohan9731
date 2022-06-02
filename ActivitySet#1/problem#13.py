# Network Programming
# https://www.py4e.com/lessons/network
name = input("Enter file:")
try:
	handle = open(name)
except:
	print("invalid input")
d={}

for line in handle:
	if line.startswith("From "):   
		line=line.split()
		line=line[5]
		line=line[:2]
		d[line]=d.get(line,0)+1
	else:
		continue        
l=list()
for key,value in d.items():
	l.append((key,value))
    
l.sort()

for key,value in l[:]:
	print(key,value)