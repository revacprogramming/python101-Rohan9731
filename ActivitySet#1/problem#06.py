def computepay(h, r):
    if h<40:
        value=h*r
    else:   
        value=40*r +(h-40)*r*1.5
    return value

hrs = float(input("Enter Hours:"))
rate = float(input("enter rate"))
p = computepay(hrs,rate)
print("Pay", p)