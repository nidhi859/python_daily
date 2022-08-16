if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    #print(student_marks)
    query_name = input()
    sum = 0
    for i in student_marks[query_name]:
        sum += i
    avg = "{:.2f}".format(sum/3)
    print(avg)