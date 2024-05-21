# #1
# print("Hello")

# #2
# print("Hello World")

# #3
# print("Hello")
# print("World")

# #4 
# print("'Hello'")

# #5
# print('"Hello World"')

# #6
# print("\"!@#$%^&*()\'")

# #7
# print("\"C:\\Download\\\'hello\'.py\"")

#8
# print("print(\"Hello\\nWorld\")")

#9
# a=input()
# print(a)

#10
# a = input()
# a = int(a)
# print(a)

#11
# a = input()
# a = float(a)
# print(a)

# 12
# a = input()
# b = input()
# a = int(a)
# b = int(b)
# print(a)
# print(b)

#13
# a = input()
# b = input()
# print(b)
# print(a)

#14
# a = input()
# a = float(a)
# print(a)

# 15
# a,b = input().split()
# print(a)
# print(b)

#16
# a,b=input().split()
# print(b, a)

# #17
# a=input()
# print(a, a, a)

# #18
# a,b=input().split(":")
# print(a,b,sep=":")

#19
# a,b,c=input().split(".")
# print(c,b,a,sep="-")

#20
# a,b = input().split("-")
# print(a,b,sep="")

# #21
# a=input()
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])

#22
# a=input()
# print(a[:2],a[2:4],a[4:])

#23
# a,b,c=input().split(":")
# print(b)

#24
# a,b=input().split()
# print(a+b)

#25
# a,b=input().split()
# c = int(a)+int(b)
# print(c)

#26
# a=float(input())
# b=float(input())
# print(a+b)

#27
# b=int(input())
# print("%x"%b)

#28
# b=int(input())
# print("%X"%b)

#29
# b=int(input(),16)
# print("%o"%b)

#30
# b=input()
# print(ord(b))

#31
# b=int(input())
# print(chr(b))

#32
# b=int(input())
# print(-b)

#33
# b=ord(input())
# print(chr(b+1))

#34
# a,b=input().split()
# print(int(a)-int(b))

#35
# a,b=input().split()
# print(float(a)*float(b))

#36
# a,b=input().split()
# print(a*int(b))

#37
# a=input()
# b=input()
# print(int(a)*b)

#38
# a,b=input().split()
# print(int(a)**int(b))

#39
# a,b=input().split()
# print(float(a)**float(b))

#40
# a,b=input().split()
# print(int(a)//int(b))

#41
# a,b=input().split()
# print(int(a)%int(b))

#42
# a=float(input())
# print("%.2f"%a)

#43
# a,b=input().split()
# c=float(a)/float(b)
# print("%.3f"%c)

#44
# a,b=map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print("%.2f"%(a/b))

#45
# a,b,c=map(int, input().split())
# cnt = (a+b+c)
# print(cnt,"%.2f"%(cnt/3))

# #46
# a=int(input())
# print(a<<1)

#47
# a,b=input().split()
# print(int(a)<<int(b))

#48
# a,b=map(int, input().split())
# if a < b:
#     print("True")
# else:
#     print("False")

#49
# a,b=map(int, input().split())
# if a == b:
#     print("True")
# else:
#     print("False")

#50
# a,b=map(int, input().split())
# if a <= b:
#     print("True")
# else:
#     print("False")

# #51
# a,b=map(int, input().split())
# if a != b:
#     print("True")
# else:
#     print("False")

#52
# a=int(input())
# if a == 0:
#     print("False")
# else:
#     print("True")

#53
# a=int(input())
# if a == False:
#     print("True")
# else:
#     print("False")

#54
# a,b=map(int, input().split())
# if a and b:
#     print("True")
# else:
#     print("False")

#55
# a,b=map(int, input().split())
# if a or b:
#     print("True")
# else:
#     print("False")

#56
# a,b=map(int, input().split())
# if a != b:
#     print("True")
# else:
#     print("False")

#57
# a,b=map(int, input().split())
# if a == b:
#     print("True")
# else:
#     print("False")

#58
# a,b=map(int, input().split())
# if not(a) and not(b):
#     print("True")
# else:
#     print("False")

#59
# a=int(input())
# print(~a)

#60
# a,b=map(int, input().split())
# print(a&b)

#61
# a,b=map(int, input().split())
# print(a|b)

#62
# a,b=map(int, input().split())
# print(a^b)

#63
# a,b=map(int, input().split())
# c = (a if a>b else b)
# print(c)

#64
# a,b,c=map(int, input().split())
# d = (a if a<b else b) if ((a if a<b else b) < c) else c
# print(d)

#65
# a,b,c = map(int, input().split())
# if a%2 == 0:
#     print(a)

# if b%2 == 0:
#     print(b)

# if c%2 == 0:
#     print(c)

# 66
# a,b,c = map(int, input().split())
# if a%2 == 0:
#     print("even")
# else: 
#     print("odd")

# if b%2 == 0:
#     print("even")
# else: 
#     print("odd")

# if c%2 == 0:
#     print("even")
# else: 
#     print("odd")

#67
# a = int(input())

# if a < 0:
#     if a%2 == 0:
#         print("A")
#     else:
#         print("B")
# else:
#     if a%2 == 0:
#         print("C")
#     else:
#         print("D")

# 68
# score = int(input())
# if 89 < score <= 100:
#     print("A")
# elif 69 < score <= 89:
#     print("B")
# elif 39 < score <= 69:
#     print("C")
# else:
#     print("D")

# 69
# char = str(input())

# if char == "A":
#     print("best!!!")
# elif char == "B":
#     print("good!!")
# elif char == "C":
#     print("run!")
# elif char == "D":
#     print("slowly~")
# else:
#     print("what?")    

#70
# month = int(input())

# if month == 12 or month == 1 or month == 2:
#     print("winter")
# elif month == 3 or month == 4 or month == 5:
#     print("spring")
# elif month == 6 or month == 7 or month == 8:
#     print("summer")
# else:
#     print("fall")    

#71
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     print(a)

#72
# a=int(input())
# while True:
#     print(a)
#     a-=1
#     if a == 0:
#         break

#73
# a=int(input())
# while a > 0:
#     a-=1
#     print(a)

#74
# a = ord(input())
# b = ord("a")

# for i in range(b,a+1):
#     print(chr(b),end=" ")
#     b+=1

#75
# n = int(input())
# for i in range(0, n+1):
#     print(i)

#76
# n = int(input())
# for i in range(0, n+1):
#     print(i)

#77
# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     if i%2 == 0:
#         sum+=i
# print(sum)

#78

# while True:
#     char = input()
#     print(char)
#     if char == "q":
#         break

#79
# num = int(input())
# cnt = 0
# sum = 0
# while True:
#     cnt+=1
#     sum += cnt    
#     if sum >= num:
#         print(cnt)
#         break

#80
# n,m = map(int, input().split())
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(i,j)

#81
# alpa = input()
# alpa = int(alpa,16)

# for i in range(1, 16):
#     print("%X"%alpa,"*","%X"%i,"=" ,"%X"%(alpa*i),sep="")

#82
# n = int(input())
# for i in range(1, n+1):
#     if i%10 == 3 or i%10 == 6 or i%10 == 9:
#         i="X"
#     print(i,end=" ")

#83
# r,g,b = map(int, input().split())
# cnt = 0
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             cnt+=1
#             print(i, j, k)
        
# print(cnt)

#84
# h,b,c,s = map(int, input().split())
# print("%.1f"%(h*b*c*s/8/1024/1024), "MB")

#85
# w,h,b = map(int, input().split())
# print("%.2f"%(w*h*b/8/1024/1024), "MB")

#86
# n = int(input())
# cnt = 0
# ran = 0
# while True:
#     ran+=1
#     cnt += ran
#     if cnt >= n:
#         print(cnt)
#         break

#87
# baesu = int(input())
# cnt = 0
# for i in range(1, baesu+1):
#     cnt+=1
#     if cnt%3 == 0:
#         continue
#     print(cnt,end=" ")

#88
# a,d,n=map(int, input().split())
# cnt = 0
# while True:
#     a+=d
#     cnt += 1
#     if cnt == n-1:
#         print(a)
#         break
    
#89
# a,r,n = map(int, input().split())
# cnt = 0
# while True:
#     a*=r
#     cnt += 1
#     if cnt == n-1:
#         print(a)
#         break

#90
# a,m,d,n = map(int, input().split())
# cnt = 0

# for i in range(n-1):
#     a = a*m+d
# print(a)

#91
# a,b,c =  map(int, input().split())
# day = 1
# while True:
#     day +=1
    
#     if day%a ==0 and day%b==0 and day%c==0:
#         print(day)
#         break

#92
# n = int(input())
# num = input().split()
# cnt = [0]*24

# for i in range(n):
#     num[i] = int(num[i])
#     cnt[num[i]] += 1   
# # print(cnt)

# for i in range(1, len(cnt)):
    
#     print(cnt[i], end=" ")

#93
# n = int(input())
# num = input().split()

# for j in range(n):
#     num[j] = int(num[j])

# for i in range(len(num)-1,-1,-1):
#     print(num[i],end=" ")

#94
# n = int(input())
# num = input().split()

# for j in range(n):
#     num[j] = int(num[j])

# for i in range(n):
#     pass
# print(min(num),end=" ")

#95
# d = [[0 for _ in range(20)] for _ in range(20)]


# doll = int(input())

# for i in range(doll):
#     x,y = input().split()
#     x=int(x)
#     y=int(y)
#     d[x][y] = 1

# for j in range(1, 20):
#     for k in range(1, 20):
#         print(d[j][k], end=" ")
#     print()

#96
# d = [[0 for _ in range(19)] for _ in range(19)]

# for k in range(19):
#     d[k] = list(map(int, input().split()))


# doll = int(input())

# for i in range(doll):
#     x,y = input().split()
#     x=int(x)
#     y=int(y)
#     for j in range(19):
#         if d[j][y-1] == 0:
#             d[j][y-1] = 1
#         else:
#             d[j][y-1] = 0

#         if d[x-1][j] == 0:
#             d[x-1][j] =1
#         else:
#             d[x-1][j] = 0

# for j in range(19):
#     for k in range(19):
#         print(d[j][k], end=" ")
#     print()

#98
# w,h = map(int, input().split())
# n = int(input())

# pan = [[0 for _ in range(h)] for _ in range(w)]

# for i in range(n):
#     l,d,x,y = map(int, input().split())

#     if d == 0:
#         for j in range(l):
#             pan[x-1][y+j-1] = 1
#     else:
#         for j in range(l):
#             pan[x+j-1][y-1] = 1


# for j in range(w):
#     for k in range(h):
#         print(pan[j][k], end=" ")
#     print()

#99
ant = [[0 for _ in range(10)] for _ in range(10)]

for i in range(10):
    ant[i] = list(map(int,input().split()))

x,y = 1,1

while True:
    if ant[x][y] == 2:
        ant[x][y] = 9
        break
    
    if ant[x][y+1] != 1:
        ant[x][y] = 9
        y+=1
    else:
        if ant[x+1][y] != 1:
            ant[x][y] = 9
            x+=1
        else:
            ant[x][y] = 9
            break


for j in range(10):
    for k in range(10):
        print(ant[j][k], end=" ")
    print()
        

