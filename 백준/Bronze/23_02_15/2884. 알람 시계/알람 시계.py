H,M = map(int,input().split())

if (M>=45) :
    M = M - 45
    print(H,M)
elif (M<45) :
    M = (M+60) - 45
    if (2<= H <= 23):
        H = H - 1
    elif (H == 1):
        H = 0
    elif (H == 0):
        H = 23
    print(H,M)
        