N = int(input())


for _ in range(N) :
    test = list(input())
    total_score = 0
    score =0

    for i in test :
        if i == 'O' :
            score += 1
        elif i ==  'X' :
            score = 0
        total_score += score
    print(total_score)

                
## for _ in  range() 에서  ' _ '는 아래 2번째 의미이며, index를 무시한다는 뜻이다.

##인터프리터(Interpreter)에서 마지막 값을 저장할 때
##값을 무시하고 싶을 때 (흔히 “I don’t care"라고 부른다.)
##변수나 함수명에 특별한 의미 또는 기능을 부여하고자 할 때
##국제화(Internationalization, i18n)/지역화(Localization, l10n) 함수로써 사용할 때
##숫자 리터럴값의 자릿수 구분을 위한 구분자로써 사용할 때
