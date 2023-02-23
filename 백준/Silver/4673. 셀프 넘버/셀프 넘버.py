def d(n) :
    return n+sum(map(int,str(n)))

num = list(range(1,10001))
not_self_num = []

for i in range(1,10_001) :
    not_self_num.append(d(i))

for i in range(1,10_001) :
    if i not in not_self_num :
        print(i)
