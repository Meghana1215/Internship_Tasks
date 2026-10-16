# Problem 16 : Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem


if __name__ == '__main__':
    students = []
    grades = []
    names = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    for i in students:
        grades.append(i[1])
    grades = sorted(set(grades))
    second_lowest = grades[1]
    for i in students:
        if i[1] == second_lowest:
            names.append(i[0])
    names.sort()
    for i in names:
        print(i)
