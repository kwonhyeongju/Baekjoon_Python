T = int(input())

for _ in range(T) :
    N = str(input())
    N_len = len(N)
    print(N[0]+N[N_len-1])