# method 1 - self
def rotation(a,n):
    b = []
    c = []
    for i in range(0,n):
        b.append(a[i])
    for i in range(n,len(a)):
        c.append(a[i])
    a = c + b
    print(a)

# method 2
# function to rotate array by d elements using temp array
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr
 
# method 3
#Function to left rotate arr[] of size n by d*/
def leftRotate(arr, d, n):
	for i in range(d):
		leftRotatebyOne(arr, n)

#Function to left Rotate arr[] of size n by 1*/
def leftRotatebyOne(arr, n):
	temp = arr[0]
	for i in range(n-1):
		arr[i] = arr[i+1]
	arr[n-1] = temp

# utility function to print an array */
def printArray(arr,size):
	for i in range(size):
		print ("%d"% arr[i],end=" ")


# method 4 --> juggling algo
#Function to left rotate arr[] of size n by d
def leftRotate2(arr, d, n):
	for i in range(gcd(d,n)):
		
		# move i-th values of blocks
		temp = arr[i]
		j = i
		while 1:
			k = j + d
			if k >= n:
				k = k - n
			if k == i:
				break
			arr[j] = arr[k]
			j = k
		arr[j] = temp

#UTILITY FUNCTIONS
#function to print an array
def printArray2(arr, size):
	for i in range(size):
		print ("%d" % arr[i], end=" ")

#Function to get gcd of a and b
def gcd(a, b):
	if b == 0:
		return a;
	else:
		return gcd(b, a%b)

a = [1,2,3,4,5,6,7]
n = int(input())
rotation(a,n)
print(rotateArray(a, len(a), 2))
ar = [1,2,3,4,5,6,7]
leftRotate(ar, 2, 7)
printArray(ar, 7)
print()
arr = [1,2,3,4,5,6,7]
leftRotate2(arr, 2, 7)
printArray2(arr, 7)