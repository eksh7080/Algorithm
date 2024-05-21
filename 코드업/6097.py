w,h = map(int, input("격자판 생성").split())
n=int(input("막대기 갯수"))

# 격자 생성
pan = [[0 for j in range(h)] for i in range(w)]


for i in range(n):
    l,d,x,y = map(int, input("막대기 길이, 방향, 행, 열").split()) # 길이 방향 좌표 입력
    if d == 0: # 가로
        for j in range(l):
            pan[x-1][y+j-1] = 1
            print(pan[x][y],pan[x][y],pan[j])
    else:   # d==1 세로
        for j in range(l):
            pan[x+j-1][y-1] = 1
            print(pan[x][y],pan[x][y],pan[j])


for i in range(w):
    for j in range(h):
        print(pan[i][j], end = " ")
    print()