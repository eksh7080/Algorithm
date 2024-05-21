d=[]
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

# d = [[0 for j in range(20)] for i in range(20)]

n=int(input())
for j in range(n):
    x,y=map(int,input().split())
    d[x][y] = 1 


for k in range(1, 20):
    for l in range(1, 20):
        print(d[k][l], end=" ")
    print()