def swapLast1(arr1):#by using * operand we can divide the list in some parts...the * one is group of rest of elements
    # here arr is the result of swapLast()
    start, *middle, end = arr1
    arr1 = [end, *middle, start]
    # print(start)
    # print(*middle)
    # print(end)
    print(arr1)

def swapLast(arr):
    length = len(arr) #or for last element wecan simply use arr[-1]
    temp = arr[0]
    arr[0] = arr[length-1]
    arr[length-1] = temp
    print(arr)

def swapLast2(list):  
    first = list.pop(0)  
    last = list.pop(-1)
    list.insert(0, last) 
    list.append(first)
    print(list)

if __name__ == "__main__":
    arr =list(map(int, input().split()))
    swapLast(arr)
    swapLast1(arr)
    swapLast2(arr)