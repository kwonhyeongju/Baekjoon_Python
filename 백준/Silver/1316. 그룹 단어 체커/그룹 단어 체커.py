N = int(input())


group_word = 0
for _ in range(N) :
    cnt = 0
    word = input()
    for index in range(len(word)-1) :
        if word[index] != word[index+1] :
            new_word = word[index+1:]
            if new_word.count(word[index]) > 0 :
                cnt += 1
    if cnt == 0 :
        group_word += 1
    
print(group_word)