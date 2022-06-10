
def add(a, b):
    return a+b


def output(a, b, sum):
    print("sum of given two numbers ",a,"and" ,b,"is",sum)


def main():
    a = float(input("input first_number:"))
    b = float(input("enter the second number:"))
    sum = add(a, b)
    output(a, b, sum)


if __name__ == '__main__':
    main()

