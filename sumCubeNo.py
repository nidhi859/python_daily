# method 1
def sumCube1(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**3
    print(sum)
# method 2
def sumCube2(n):
    sum = (n * (n + 1)  / 2)
    print(int(sum*sum))

# method 3 --> to avoid overflow in method 2
def sumCube3(n):
    x = 0
    if n % 2 == 0 :
        x = (n/2) * (n+1)
    else:
        x = ((n + 1) / 2) * n
         
    print(int(x * x))

n = int(input())
sumCube1(n)
sumCube2(n)
sumCube3(n)