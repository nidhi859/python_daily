# Reverse the first ‘d’ elements
# Reverse last (N-d) elements
# Reverse the whole array.
def reverse(arr,start,end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1

def rotate(arr,d,n):
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
    print(arr)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    d = int(input())
    n = len(arr)
    rotate(arr,d,n)