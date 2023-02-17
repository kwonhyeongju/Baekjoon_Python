N = int(input())
lst = list(map(int,input().split()))

max = lst[0]
min = lst[0]

for i in range(N) :
    if max<lst[i] :
        max = lst[i]
    if min>lst[i] :
        min = lst[i]

print(f'{min} {max}')