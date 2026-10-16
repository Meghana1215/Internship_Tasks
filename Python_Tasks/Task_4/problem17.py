# Problem 17 : Finding the Percentage
# https://www.hackerrank.com/challenges/finding-the-percentage/problem


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        data = input().split()
        name = data[0]
        scores = list(map(float, data[1:]))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    avg = sum(marks) / len(marks)
    print("{:.2f}".format(avg))
