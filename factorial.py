import math
if __name__ == "__main__":
    # factorial using recurisve function:
    def fact(x):
        if(x < 0):
            return 0
        elif(x == 1 or x == 0 ):
            return 1
        else:
            return(x*fact(x-1))
    
    # factorial using while loop
    def fact2(n):
        if n < 0:
            return 0
        elif n == 0 or n == 1:
            return 1
        else:
            fact = 1
            while(n > 1):
                fact *= n
                n -= 1
            return fact
    
    # factorial using for loop
    def fact3(x):
        factorial = 1
        if(x < 0):
            return 0
        elif(x == 0 or x == 1):
            return 1
        else:
            for i in range(1,x + 1):
                factorial = factorial*i
            return factorial
    
    a = int(input())    
    print(fact(a))
    print(fact2(a))
    print(fact3(a))
    # factorial using in-built function
    print(math.factorial(a))
    

