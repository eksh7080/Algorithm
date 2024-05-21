"""
같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 문제를 푸는 날짜가
매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?

예를 들어 3명이 같은 날 가입/등업하고, 각각 3일마다, 7일마다, 9일마다
한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게 된다.

day는 날 수, a/b/c는 방문 주기이다.
...
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)
...

"""
# a,b,c=map(int,input().split())

# day = 1

# while True:
#     if day%a==0 and day%b==0 and day%c==0:
#         print(day)
#         break
    
#     day+=1
    

a,b,c=map(int,input().split())

day = 1

while day%a!=0 or day%b!=0 or day%c!=0:
    day+=1
print(day)

