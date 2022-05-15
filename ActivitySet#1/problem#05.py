from wsgiref.util import FileWrapper


score = float(input("Enter Score: "))
if score<0 or score>1.0:
    print('enter the score between 0.0 and 1.0')
elif score>=0.9 and score<1.0:
    print("A GRADE")
elif score>=0.8:
     print("B GRADE")
elif score>=0.7:
    print("C GRADE")
elif score>=0.6:
    print("D GRADE")
else:
    print("FAIL")