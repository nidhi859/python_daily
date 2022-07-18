def largest(a):
   x = -1
   for i in range(len(a)):
       if(a[i]>x):
            x = a[i]
   print(x)
def largest2(a):
    x = max(a)
    print(x)

a = [1,4,2,9,40,2,4]
largest(a)
largest2(a)