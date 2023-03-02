default = ['c=', 'c-','dz=','d-','lj','nj','s=','z=']
word = input()

for i in default :
    word = word.replace(i,'*')

print(len(word))