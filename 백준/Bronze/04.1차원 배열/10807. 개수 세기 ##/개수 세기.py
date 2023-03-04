N = int(input())
lst = list(map(int,input().split()))
v = int(input())

cnt = 0

for i in lst :
    if i == v:
        cnt += 1

print(cnt)

## Python3에서는 리스트의 특정 엘리먼트의 반복 회수를 세는 빌트인 count 함수를 사용하면 간편하게 해결가능
## print(lst.count(v))
