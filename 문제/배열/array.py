# import sys
# input = sys.stdin.readline

# 10818
# n = int(input())
# a = list(map(int, input().split()))
# print(min(a),max(a))

# 2562

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# f = int(input())
# g = int(input())
# h = int(input())
# i = int(input())
# sum = [a,b,c,d,e,f,g,h,i]
# print(sum)
# print(max(sum))
# print(sum.index(max(sum))+1)

# numbers = []
# for i in range(9):
#     a = int(input())
#     numbers.append(a)
# print(max(numbers))
# print(numbers.index(max(numbers))+1)

# num = [int(input()) for i in range(9)]
# print(max(num))
# print(num.index(max(num))+1)

# 2577
# a = input()
# b = input()
# c = input()
# sum = [] 
# sum.append(int(a)*int(b)*int(c))
# sum = str(sum)

# string = ''.join(sum)

# for i in range(10):
#     print(string.count('%d'%i))

# 3052
# num = []
# for i in range(10):
#     a=int(input())
#     sum = a%42
#     num.append(sum)

# # set = 중복 허용 하지 않음
# num = set(num)
# print(len(num))

# 1546
# num = int(input())
# score = list(map(int, input().split()))
# data = []
# average = 0
# for i in range(num):    
#     sum = score[i]/max(score)*100
#     data.append(sum)
#     average += data[i]
    
# print(average/num)

# 8958
# test = int(input())

# for i in range(test):
#     cnt = 0
#     sum = 0
#     case = list(input())
#     for j in case:
#         if j == "O":
#             cnt += 1
#             sum += cnt
#         else:
#             cnt = 0
#     print(sum)

# 4344
# test = int(input("테스트 케이스:"))

# for i in range(test):
#     stu = list(map(int, input().split()))
#     cnt=0
#     score = stu[1:]
#     hap = (sum(score)/(len(score)))
    
#     for j in score:
#         if j > hap:
#             cnt+=1
#     baek = cnt/len(score)*100
#     print(f"{baek:0.3f}%")































