X = []

X = [i for i in range(1,31)]

for i in range(28):
    submit = int(input())
    X.remove(submit)

print(min(X),max(X),end = "\n")



