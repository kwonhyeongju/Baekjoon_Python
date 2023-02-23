T = int(input())

for _ in range(T) :
    R,S = input().split()
    R = int(R)
    S = str(S)

    for i in range(len(S)) :
        cnt = 0
        while(cnt != R) :
            print(S[i],end = "")
            cnt += 1
    print()
            