# Use the file name mbox-short.txt as the file name
count=0
total=0

fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
    print("entered file is invalid/not found:",fname)
for line in fh:
	if line.startswith("X-DSPAM-Confidence:"):
		count=count+1
		digit= line.find(":")
		x= float(line[digit+1:])
		total= total+x
	else:
		continue
        
value = total/count        
        
print("Average spam confidence:",value)

