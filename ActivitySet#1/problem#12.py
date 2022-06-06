# Regular Expressions
# https://www.py4e.com/lessons/regex
name = input("Enter file:")
try:
	handle = open(name)
except:
    print("entered file is invaild")
count ={}
lst=list()
for line in handle:
	if line.startswith("From: "):
		line = line.split()
		lst.append(line[1])
	else:
		continue        
for word in lst:
	count[word] = count.get(word,0)+1
#print(words)
bigcount = None
bigword = None
for word,val in count.items():
    if bigcount is None or val > bigcount:
        bigcount = val
        bigword = word
print(bigword , bigcount)			
				
    