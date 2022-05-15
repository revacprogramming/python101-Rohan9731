# Conditional Execution

hrs = (input("Enter hours? "))
rate= (input("enter rate:"))
if (hrs<=40):
    x=hrs*rate
elif(hrs>40):x=hrs*rate + (hrs-40)*1.5*rate
print("pay:",x)