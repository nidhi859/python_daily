# method 1
if __name__ == "__main__":
    def armstrong(n):
        sum = 0
        for i in n:
            a = int(i)**3
            sum += a
        if(sum == int(n)):
            print(f"{n} is an armstrong no.")
        else:
            print(f"{n} is not an armstrong no.")

# method 2    
n = input()
armstrong(n)
n = 153 
s = n  
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1+(r**b)
    n = n//10
if s == sum1:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")