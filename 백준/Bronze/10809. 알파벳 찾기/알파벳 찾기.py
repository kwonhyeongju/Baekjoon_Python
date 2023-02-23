S = str(input())

for i in range(97,123) :
    print(S.find(chr(i)),end = " ")
    
## find() 와 index()

## 공통점
##'변수. find(찾을 문자)' / '변수. index(찾을 문자)' 

## 차이점
## find() 는 찾는 문자가 없는 경우에 -1을 출력한다.
## index() 는 찾는 문자가 없는 경우에 ValueError 에러가 발생한다.
