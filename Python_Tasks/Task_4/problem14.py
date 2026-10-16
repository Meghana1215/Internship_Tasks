# Problem 14 : Set .add()
# https://www.hackerrank.com/challenges/py-set-add/problem


N = int(input())
s = set()
for i in range(N):
    country = input().strip()
    s.add(country)
print(len(s))
 
