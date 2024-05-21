# 개미집 생성
antHouse = [[0 for j in range(10)] for i in range(10)]

# 개미집 입력
for i in range(10):
    antHouse[i] = list(map(int,input().split()))
    
# 줄바꿈
print()

# 개미 시작 위치 list 이기 때문에 2,2 는 1,1 이다.
x,y = 1,1


while True:
    if antHouse[x][y] == 2: # 개미가 멈춰야 할 때
        antHouse[x][y] = 9 # 먹이로 이동했으니 9로 바꿔줘야 함
        break
    elif (x,y) == (8,8):
        break

# 개미가 이동 경로 증가
    if antHouse[x][y+1] != 1:
        antHouse[x][y] = 9
        y+=1
    else:
        if antHouse[x+1][y] != 1:
            antHouse[x][y] = 9
            x+=1
        else:
            antHouse[x][y]=9
            break

# 이중 반복문으로 출력
for i in range(10):
    for j in range(10):
        print(antHouse[i][j], end =" ")
    print()