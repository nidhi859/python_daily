def limitFibonacci(n):
    L = [0,1]
    sum = 0
    if n<= 0:
        return "Incorrect Output"
    if(n>2):
        for i in range(2,n+1):
            sum = L[i-1] + L[i-2]
            L.append(sum)

    print(L[n])

n = int(input())
limitFibonacci(n)
