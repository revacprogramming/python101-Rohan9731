count=0
fname = input("Enter file name: ")
try:
    file=open(fname)
except:
    print("Entered file is not exist")

for line in file:
    if line.startswith('From '):
        word=line.rstrip().split()
        count=count+1
        print(word[1])
    else:
        continue
   

print("There were", count, "lines in the file with From as the first word")


