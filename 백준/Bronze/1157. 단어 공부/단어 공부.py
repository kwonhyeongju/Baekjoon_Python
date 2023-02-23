S = str(input().upper())  # baaa # BAAA
unique_S = list(set(S))  # ['B','A']

cnt_S = []
for i in unique_S :  # i = B,A
    cnt = S.count(i)    
    cnt_S.append(cnt)   #[1,3]

if cnt_S.count(max(cnt_S)) > 1 :
    print('?')

else :
    print(unique_S[cnt_S.index(max(cnt_S))]) 
