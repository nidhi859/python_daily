def replace(arr,m):
    for i in range(len(arr)):
        if(arr[i]==-1):
            arr[i] = (arr[i-1]+1)%m
    print(arr)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    m = int(input())
    replace(arr,m)