'''Can be solved in 2 parts:
1st part:
1.Take name and score as input
2.Store name and score in nested list `li`
3.Make a Unique_sorted_score_list that is unique(using set()) and sorted(using sorted()) scores
4.Fetch second_lowest_score from Unique_sorted_score_list
2nd part:
1.create an empty list => list
2.for every student in `li`
3.check if second_lowest_score match any student[score]
4.if Yes: append in student_list
5.iterate through `list` to print result
'''
if __name__ == '__main__':
   
    n = int(input())
    li = []
    for i in range(n):
        name = input()
        score = float(input())
        li.append([name,score])
    scores = sorted(list(set([x[1] for x in li])))
    #print(scores)
    second_lowest = scores[1]
    #print(second_lowest)

    list = []
    for student in li:
        if second_lowest == student[1]:
            list.append(student[0])
    #print(list)
    for student in sorted(list):
        print(student)