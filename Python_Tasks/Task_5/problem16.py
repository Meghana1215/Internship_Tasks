# Problem 16 : collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem


from collections import Counter
X = int(input())
shoes = list(map(int, input().split()))
sizes = Counter(shoes)
N = int(input())
total = 0
for i in range(N):
    size, price = map(int, input().split())
    if sizes[size] > 0:
        total += price
        sizes[size] -= 1
print(total)
