while 1 :
    try: 
        A,B = map(int,input().split())
    except :
        break
        
    print(A+B)
    
    ## try 구문에는 에러가 발생할 여지가 있는 문장을 작성하고 except 구문에는 에러가 발생 시 실행시킬 문장을 작성한다. 
    ## 여기에선 break로 빠져나가도록 했다.
    ## 만일 아무런 에러가 발생하지 않는 경우 except 구문을 지나쳐서 이후의 print(a+b) 코드를 마저 실행시킨다.
