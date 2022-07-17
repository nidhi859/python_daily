import math
if __name__ == "__main__":
    def area(r):
        a = 3.14*r*r
        print(a)
        area = math.pi* pow(r,2)
        print(area)
    n = int(input())
    area(n)