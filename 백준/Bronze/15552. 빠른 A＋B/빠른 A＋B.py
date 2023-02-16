import sys

T = int(input())

for i in range(T) :
    A,B = map(int,sys.stdin.readline().split())         ## 내장함수 input()과 달리 sys.stdin은 file object이며, 사용자의 입력을 받는 buffer를 그 buffer에서 읽어들이는 것이다.
    print(A+B)                                          ## 그래서 input()은 raw_input()을 evaluate 한 결과를 반환하고, sys.stdin.readline()은 한 줄의 문자열을 반환한다.
                                                        ## 버퍼에 보관하고 사용자가 요구할 때 버퍼에서 읽어오게 하는 것이 더 빠르다.
