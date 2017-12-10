# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter

def solution(A):
    return min([helper(i, A) for i in range(7)])

def helper(n, A):
    ret = 0
    for i in A:
        if i == abs(n-7):
            ret += 2
        elif i != n:
            ret += 1
    return ret


print(solution([1, 1, 6, 6]))

print(solution([1, 6, 2, 3])) 