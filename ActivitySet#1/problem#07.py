largest =None
smallest=None

while True:
    num =(input("Enter a number: "))	
    if num == 'done':
        break        
    try:
        x=int(num)
    except:
        print("Invalid input")
    if largest is None or largest < x:
            largest =x
    if smallest is None or smallest > x:
            smallest=x         
    

print ("Maximum is", largest)
print ("Minimum is", smallest)