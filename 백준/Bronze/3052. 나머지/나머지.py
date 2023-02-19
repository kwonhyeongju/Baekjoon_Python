X = []

X = [int(input())% 42 for i in range(0,10)]

Y = set(X)

print(len(Y))

## 중복을 허용하지 않는 set의 특징은 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용
