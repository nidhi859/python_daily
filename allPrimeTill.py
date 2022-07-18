if __name__ == "__main__":
    def checkPrime(n):
        if(n == 0 or n == 1):
            return False
        else:
            for i in range(2,((n//2)+1)):
                if(n%i == 0):
                    return False
            else:
                return True

    n = int(input())
    for i in range(1,n+1):
        if(checkPrime(i)):
            print(i, end=" ")