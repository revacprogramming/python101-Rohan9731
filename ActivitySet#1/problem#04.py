# Conditional Execution

hrs = float(input("Enter hours? "))
rate= float(input("enter rate:"))
if (hrs<=40):
    x=hrs*rate
else:
    x =40*rate + (hrs-40)*1.5*rate
print("pay:",x)