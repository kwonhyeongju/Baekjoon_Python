N = int(input())

for i in range(1,N+1):
    for j in range(1,i+1) :
        print("*",end = "")
    print()
    
    ## 파이썬의 경우 문자열을 더하고 곱할 수 있다는 강점이 있고, 직관성이 있는 언어입니다.
    ## for i in range(1,(N+1)):
    ##     print("*" * i)
