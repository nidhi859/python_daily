# can give the problem of overflow
from cv2 import reduce


def remainder(arr,n):
    mul = 1
    for i in range(len(arr)):#mul = reduce(lambda x,y:x*y,arr)
        mul *= arr[i]        # here x and y are the first two elements of sequence
    result = mul%n
    print(result)

from functools import reduce
# remove the problem of overflow --> first take remainder of each individual element of array
# then multiply each remainder then finally calculate the remainder 
def remainder1(arr,n):
    # mul = 1
    # for i in range(len(arr)):
    #     mul *= arr[i]%n
    # result = mul%n
    # print(result)
    mul = reduce(lambda x,y:x*y%n,arr) #reduce function is used to apply a particular functon passed in its argument to all the list elements
    result = mul%n
    print(result)

if __name__ == "__main__":
    n = int(input())
    arr= list(map(int, input().split()))
    remainder(arr,n)
    remainder1(arr,n)
    