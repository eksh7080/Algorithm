"""
예시
...
for i in range(n) :
  x,y=input().split()
  for j in range(1, 20) :
    if d[j][int(y)]==0 :
      d[j][int(y)]=1
    else :
      d[j][int(y)]=0

    if d[int(x)][j]==0 :
      d[int(x)][j]=1
    else :
      d[int(x)][j]=0
...

참고
리스트가 들어있는 리스트를 만들면?
가로번호, 세로번호를 사용해 2차원 형태의 데이터처럼 쉽게 기록하고 사용할 수 있다.
리스트이름[번호][번호] 형식으로 저장되어있는 값을 읽고 쓸 수 있다.
"""

n=[]

for i in range(20):
    n.append([])
    for j in range(20):
        n[i].append(0)

for i in range(19):
    n[i] = list(map(int, input().split()))

p = int(input())

for i in range(p):
    x,y=map(int,input().split())
    for j in range(19):
        if n[j][y-1] == 0:
            n[j][y-1] = 1
        else:
            n[j][y-1] = 0
            
        if n[x-1][j] == 0:
            n[x-1][j] = 1
        else: n[x-1][j] = 0

for i in range(19):
    for j in range(19):
        print(n[i][j], end=" ")
    print() 

