largest =0
smallest=0

while True:
    num = (input("Enter a number: "))	
    if num == 'done':
        break        
    try:
        x=int(num)
        if largest is 0 or largest < x:
            largest =x
        if smallest is 0 or smallest > x:
            smallest=x 
    except:
        print("Invalid input")
    continue 

print ("Maximum is", largest)
print ("Minimum is", smallest)