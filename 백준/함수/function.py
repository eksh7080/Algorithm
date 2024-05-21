# 15596
# a = list(map(int, input().split()))

# def solve(a):
#     ans = 0
#     for i in a:
#         ans+=i
#     return ans

# ans = solve(a)
# print(ans)

# def solve(a):
#     ans = 0
#     for i in a:
#         ans+=i
#     return ans

# 4673

# def selfnum(n):
#     num = n
#     for i in list(str(n)):
#         num += int(i)
#     return num

# numbers = set(range(1, 10000))
# newArr = set()
# for j in range(1, 10000):
#     newArr.add(selfnum(j))

# numself = sorted(numbers - newArr)
# for i in numself:
#     print(i)

# numbers = set(range(1, 10000))
# newSet = set()

# for i in range(1, 10000):
#     for j in str(i):
#         i += int(j)
#     newSet.add(i)

# nonSelf = (numbers - newSet)
# for i in sorted(nonSelf):
#     print(i)

# 1065

# def han(mod):
#     cnt = 0
#     for i in range(1, mod+1):
#         if i < 100:
#             cnt+=1
#         else:
#             num = list(map(int, str(i)))
#             if num[0] - num[1] == num[1] - num[2]:
#                 cnt+=1
#     return cnt 

# mod = int(input())
# print(han(mod))


# mod = int(input())
# cnt = 0

# for i in range(1, mod+1):
    
#     if i < 100:
#         cnt+=1
#     else:
#         num = list(map(int, str(i)))

#         if num[0] - num[1] == num[1] - num[2]:
#             cnt+=1

# print(cnt)
