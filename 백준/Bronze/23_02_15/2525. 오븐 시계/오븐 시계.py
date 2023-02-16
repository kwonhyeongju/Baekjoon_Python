A,B = map(int,input().split())
C = int(input())

a = int((C/60))
b = (C%60)

if (B+b)>=60:
    A = A+(a+1)
    B = (B-60)+b
elif (B+b)<60:
    A = A+a
    B = B+b

if (A>=24):
    A = A-24
print(A,B)
    