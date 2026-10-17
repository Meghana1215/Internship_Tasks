# Problem 7 : Symmetric Difference.
# https://www.hackerrank.com/challenges/symmetric-difference/problem


M=int(input())
a=set(map(int,input().split()))
N=int(input())
b=set(map(int,input().split()))
c=[]

def symmetric_difference(a,b):
    for i in a:
        if i not in b:
            c.append(i)
    for i in b:
        if i not in a:
            c.append(i)
    for i in sorted(c):
        print(i)
symmetric_difference(a,b)
