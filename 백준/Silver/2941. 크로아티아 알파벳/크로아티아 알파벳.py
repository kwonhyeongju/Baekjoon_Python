default = ['c=', 'c-','dz=','d-','lj','nj','s=','z=']
word = input()

for i in default :
    word = word.replace(i,'*')

print(len(word))


## .replace()
## 문자열 안에서 특정 문자를 새로운 문자로 변경하는 기능
## replace(old, new, [count]) 형식
