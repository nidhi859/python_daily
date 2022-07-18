# method 1
def sumSquare1(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    print(sum)
# method 2
def sumSquare2(n):
    sum = (n*(n+1)*(2*n+1))//6
    print(sum)

n = int(input())
sumSquare1(n)
sumSquare2(n)

