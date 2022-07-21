# Problem 1: Rectangle Area
# Develop a program that, given as input the cartesian coordinates of three vertices of a rectangle,
# reports the area of that rectangle. You will recall that the area of a rectangle is the product of
# the lengths of any two adjacent sides.


# Input: The first line contains a positive integer n indicating how many rectangles are to be
# analyzed. Each rectangle is described on a single line via six real numbers, x1, y1, x2, y2, x3,
# and y3, separated by spaces. These provide the coordinates of three of the rectangle’s vertices,
# namely P1(x1, y1), P2(x2, y2), and P3(x3, y3).


# Output: For each rectangle provided as input, report its area.
# Sample input
# ------------
# 3
# 0.0 0.0 0.0 1.0 1.0 0.0
# -1.0 2.0 3.0 5.0 1.0 1.0
# 5.0 9.0 -0.5 0.0 7.5 5.0


class Rectangle:
    def __init__(self, veritces: list[tuple[float, float]]):
        self.v1, self.v2, self.v3 = veritces
        self.l, self.b = self.get_l_b()

    def get_l_b(self):
        x = ((self.v2[0] - self.v1[0]) ** 2 + (self.v2[1] - self.v1[1]) ** 2) ** 0.5
        y = ((self.v3[0] - self.v2[0]) ** 2 + (self.v3[1] - self.v2[1]) ** 2) ** 0.5
        z = ((self.v1[0] - self.v3[0]) ** 2 + (self.v1[1] - self.v3[1]) ** 2) ** 0.5

        if x >= y and x >= z:
            return y, z
        elif y >= z:
            return x, z
        else:
            return x, y

    def find_area(self):
        return self.l * self.b


class Rectangles(list):
    def __init__(self, rects: list[list[tuple[float, float]]]):        
        super().__init__(Rectangle(r) for r in rects)


def inp_rects():
    while True:
        try:
            n = int(input())
            assert n > 0
            break
        except:
            print("Enter a valid number of rectangles.")
            continue
 
    i = 0
    lst = []
    while True:
        try:
            nums = [float(_) for _ in input().strip().split()]
        except:
            print("Enter valid cartesian coordinates.")
            continue
        
        if (len(nums) != 6):
            print("There should only be 3 vertices with 6 total points.")
            continue
        lst.append([(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)])
        i += 1
        if i == n:
            break
        
    return lst
    
    
def output(rects):
    for rect in rects:
        print(f"Area of rectangle with vertices {rect.v1},{rect.v2},{rect.v3} is {round(rect.find_area(), 1)}")


def main():
    r = Rectangles(inp_rects())
    output(r)

if __name__ == "__main__":
    main()