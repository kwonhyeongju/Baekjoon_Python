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

                
