# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    N = int(input())
    li = []
    for i in range(N):
        opt, *value = input().split()
        val = list(map(int, value))
        if(opt == 'insert'):
            li.insert(val[0],val[1])
        elif(opt == 'print'):
            print(li)
        elif(opt == 'remove'):
            li.remove(val[0])
        elif(opt == 'append'):
            li.append(val[0])
        elif(opt == 'sort'):
            li.sort()
        elif(opt == 'pop'):
            li.pop()
        elif(opt == 'reverse'):
            li.reverse()
        
        
