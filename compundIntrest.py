import math
if __name__ == "__main__":
    p = int(input())
    r = float(input())
    t = int(input())
    A = p*(pow((1+(r/100)),t))
    print(A-p)

    