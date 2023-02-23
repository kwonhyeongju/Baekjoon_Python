def d(n) :
    return n+sum(map(int,str(n)))

num = list(range(1,10001))
not_self_num = []

for i in range(1,10_001) :
    not_self_num.append(d(i))

for i in range(1,10_001) :
    if i not in not_self_num :
        print(i)

       
## 각자리수 더 하기
## sum(map(int,str(num)))
## 생성자를 구할려면 각 자리수 분산이 가능해야하는데 이는 intu형에서는 불가능,str형에서는 가능

## map함수
## <map함수>
##정의 : 리스트의 요소를 지정된 함수로 처리해주는 함수
##활용 : 리스트의 모든 요소를 정수로 변환하기
##         >>> a = [1.2, 2.5, 3.7, 4.6]
##         >>> a = list(map(int, a))
##         >>> a
##         [1, 2, 3, 4]
