N = int(input())

for i in range(N):
    print("*" * (i+1))
    
    ## 파이썬의 경우 문자열을 더하고 곱할 수 있다는 강점이 있다.
    ## 기타 언어들의 경우 for 이중 구문을 사용해야한다.
    ## for i in range(1,N+1) :
    ##     for j in range(1,i+1) :
    ##         print("*",end = "")
    ##     print()
