# Problem 20 : Pilling Up!
# https://www.hackerrank.com/challenges/piling-up/problem


from collections import deque

for _ in range(int(input())):
    n = int(input())
    blocks = deque(map(int, input().split()))
    top = float('inf')
    for i in range(n):
        if blocks[0] >= blocks[-1]:
            cube = blocks.popleft()
        else:
            cube = blocks.pop()
        if cube > top:
            print("No")
            break
        top = cube
    else:
        print("Yes")
