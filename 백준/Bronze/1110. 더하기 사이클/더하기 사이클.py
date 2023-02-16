N = int(input())
count = 0
key = N

while 1 :
    
    count +=1
    Sum = N//10 + N%10
    N = 10*(N%10) + (Sum)%10
    if (N == key) :
        break    
    

print(count)
    
    