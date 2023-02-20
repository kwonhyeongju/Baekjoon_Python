
C = int(input())

for _ in range(C) :
    N = list(map(int, input().split()))
    avg = sum(N[1:])/N[0]

    cnt = 0
    for i in N[1:] :
        if i > avg :
            cnt += 1

    rate = (cnt/N[0])*100
    print(f'{rate:.3f}%')
    
    ## print()에서 소수점 표현 방법. f-string에서 {변수:.3f}% 꼴로 표현
    ## case[1:] 과 같은 방법으로 첫 번째 요소를 제외할 수 있다
