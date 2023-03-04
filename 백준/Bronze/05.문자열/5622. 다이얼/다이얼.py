dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

test = input()

total = 0

for i in range(len(test)) :
    for j in dial :
        if test[i] in j :
            total += 3 + dial.index(j)

print(total)
