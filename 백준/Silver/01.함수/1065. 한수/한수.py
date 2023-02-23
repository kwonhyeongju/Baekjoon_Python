N = int(input())

hansu = []
for i in range(1,N+1) :
    num_digit = list(map(int,str(i)))
    if 1 <= i < 100 :
        hansu.append(i)
    elif (num_digit[0] - num_digit[1]) == (num_digit[1] - num_digit[2]) :
        hansu.append(i)

print(len(hansu))



    