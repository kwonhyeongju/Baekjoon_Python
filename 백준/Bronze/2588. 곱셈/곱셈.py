A = int(input())
B = input()

AxB2 = A*int(B[2])
AxB1 = A*int(B[1])
AxB0 = A*int(B[0])
AxB = A*int(B)
print(AxB2,AxB1,AxB0,AxB, sep ='\n')

#배운점 : 문자열 B를 B[2] B[1] B[0] 으로 나눠 int()를 사용해 곱셈연산에 사용할 수 있다.
#배운점 : print()안에서 sep 를 통해 출력형태를 정할 수 있다.
