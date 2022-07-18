def sumArray(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    print(sum)

c = [1,4,2,5,6]
sumArray(c)
print(sum(c))