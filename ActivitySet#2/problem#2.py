
def add(a, b):
    return a+b


def output(a, b, sum):
    print("sum of given two numbers is",sum)


def main():
    a = float(input("inputtwo_numbers:"))
    b = float(input("enterthe secomd number:"))
    sum = add(a, b)
    output(a, b, sum)


# if __name__ == '__main__':
#     main()
