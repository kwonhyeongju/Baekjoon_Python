N = int(input())

Max = 2*N -1  

for i in range(N) :
    print(" "*(N-(i+1))+"*"*(2*i+1))

for j in range(N) :
    print(" "*(j+1)+"*"*(Max-(2*(j+1))))
      