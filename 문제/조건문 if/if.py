# 1330
# a,b = map(int, input().split())
# if a>b:
#     print(">")
# elif a<b:
#     print("<")
# elif a==b:
#     print("==")

# 9498
# score = int(input())
# if 90 <= score <= 100:
#     print("A")
# elif  80<= score <= 89:
#     print("B")
# elif  70<= score <= 79:
#     print("C")
# elif  60<= score <= 69:
#     print("D")
# else:
#     print("F")

# 2753
# year = int(input())
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("1")
# else:
#     print("0")

# 14681
# x=int(input())
# y=int(input())

# if 0 <= x <= 1000 and 0 <= y <= 1000:
#     print("1")
# elif 0 > x and 0 <= y:
#     print("2")
# elif 0 > x and 0 > y:
#     print("3")
# else:
#     print("4")

# 2884
# h,m = map(int, input().split()) 

# if m >= 45:
#     print(h,m-45)
# elif h > 0 and m < 45:
#     h-=1
#     print(h,m+15)
# else:
#     print(23,m+15)

# 2525
# h,m = map(int, input().split(" "))
# cook = int(input())

# h += cook // 60
# m += cook % 60

# if m >= 60:
#     h+=1
#     m -= 60

# if h >= 24:
#     h -= 24

# print(h,m)

# 2480
# a,b,c = map(int, input().split())
# same = a == b == c
# diff1 = a == b
# diff2 = a == c
# diff3 = b == c
# if same:
#     print(10000+a*1000)
# elif diff1:
#     print(1000+a*100)
# elif diff2:
#     print(1000+a*100)
# elif diff3:
#     print(1000+b*100)
# else:
#     print(max(a,b,c)*100)
