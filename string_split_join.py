def split_and_join(line):
    li = list(map(str,line.split()))
    # print(li)
    return("-".join(li))
    
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
