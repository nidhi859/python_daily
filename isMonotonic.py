def isMonotonic(A):
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
  
if __name__ == "__main__":
    A = list(map(int, input().split()))
    print(isMonotonic(A))