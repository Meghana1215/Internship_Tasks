# Problem 6 : Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
arr = list(map(int, input().split()))
first=max(arr)
while first in arr:
    arr.remove(first)
print(max(arr))
