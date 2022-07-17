# method 1
if __name__ == "__main__":
    def pattern(n):
        x = [int(i) for i in str(n)]
        for i in range(len(x)):
            print("|", end="")
            while( x[i] > 0):
                print("*",end="")
                x[i] = x[i]-1
            print()
    a = input()
    pattern(a)


# method 2
def pattern(n):
	for i in n:

		print("|", end = "")
		print("*" * int(i))
	
n = "41325"
pattern(n)


# method 3
n = 41325
x = []
while n>0:
    x.append(n%10)
    n //= 10
for i in range(len(x)-1,-1,-1):
    print('|'+x[i]*'*')