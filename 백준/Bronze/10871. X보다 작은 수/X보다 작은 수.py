N,X = map(int,input().split())
A = list(map(int,input().split()))

cnt = 0
for i in A :
    if X>i :
        print(i,end = " ")
