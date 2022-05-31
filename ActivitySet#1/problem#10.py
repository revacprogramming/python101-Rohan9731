fname = input("Enter file name: ")
try:
	fh = open(fname)
    	#lst = list()
        
except:
    print("Entered file is invalid")
lst = list()
for line in fh:
    words=line.rstrip().split()
    #words=line.split()
    for word in words:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()        
print(lst)
#print(lst)