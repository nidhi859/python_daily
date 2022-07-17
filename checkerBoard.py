# printing checkerbox using for loops
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        if(i%2 ==0):
            for j in range(n):
                if(j%2 == 0):
                    print("0 ", end="")
                else:
                    print("1 ", end="")
            print()
        else:
            for j in range(n):
                if(j%2 != 0):
                    print("0 ", end="")
                else:
                    print("1 ", end="")
            print()

# printing checkerbox using numpy library
import numpy as np
  
# function to print Checkerboard pattern
def printcheckboard(n):
      
    print("Checkerboard pattern:")
  
    # create a n * n matrix
    x = np.zeros((n, n), dtype = int)
  
    # fill with 1 the alternate rows and columns
    x[1::2, ::2] = 1
    x[::2, 1::2] = 1
      
    # print the pattern
    for i in range(n):
        for j in range(n):
            print(x[i][j], end =" ") 
        print() 
  
  
# driver code
n = 8
printcheckboard(n)
