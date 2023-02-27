import sys

N,M = map(int,sys.stdin.readline().split())

Num = [i for i in range(1,N+1)]

for _ in range(M) :
    i,j,k = map(int,sys.stdin.readline().split())
    i,j,k = i-1,j-1,k-1
    Num = Num[:i] + Num[k:j+1] + Num[i:k] + Num[j+1:]

print(*Num)