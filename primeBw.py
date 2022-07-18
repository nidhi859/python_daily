if __name__ == "__main__":
    def primebw(x,y):
        for i in range(x, y):
            if i == 0 or i == 1:
                continue
            else:
                for j in range(2, int(i/2)+1):
                    if i % j == 0:
                        break
                else:
                    print(i,end=" ")
            
    
    a = int(input())
    b = int(input())
    primebw(a,b)
    
