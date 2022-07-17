if __name__ == "__main__":
    num1 = 5
    num2 = 3
    sum = num1 + num2
    sum2 = lambda num1, num2 : num1 + num2
    # printing result generated using lambda function
    print(sum2)
    # printing result using format function
    print("sum of {0} and {1} is {2}".format(num1, num2, sum))
    # normal printing of result
    print(num1 + num2)
    # printing result using f string
    print(f"sum of {num1} and {num2} is {sum}")
    a= int(input())
    b = int(input())
    print(a + b)
    # taking multiple inputs: 
    # using split() --> will give a list; and using map function
    # to Returns a list of the results after applying the given function  
    # to each item of a given iterable (lst, tuple etc.)
    x= list(map(int, input().split()))
    print(x)
    sum3 = 0
    for i in range(len(x)):
        sum3 += x[i]
    print(sum3)
    # taking input using list comprehension
    y = [int(x) for x in input().split()]
    print(x)
    sum4 = 0
    for i in range(len(y)):
        sum4 += y[i]
    print(sum4)