# import sys
# input = sys.stdin.readline

# import string
# string.ascii_lowercase

# 11654
# a = input()
# print(ord(a))

# 11720
# a = int(input())
# b = map(int,input().strip())
# print(sum(b))

# n = int(input())
# s = str(input()) #list 도 가능
# sum = 0
# for i in range(n):
#     sum += int(n[i])
# print(sum)

# 10809
# word = list(input())
# aski = 97
# pr=[]

# for i in range(26):
#     if chr(aski) in word:
#         pr.append(word.index(chr(aski)))
#     else:
#         pr.append("-1")
#     aski+=1

# for i in range(26):
#     print(pr[i],end=" ")

# word = input()
# aski = list(range(97,123))

# for i in aski:
#     print(word.find(chr(i)),end=" ")

# 2675
# test = int(input())

# for i in range(test):
#     r,s = input().split()
#     r=int(r)
#     for j in range(len(s)):
#         print(s[j]*r,end="")
#     print()

# 1157

# alpa = input().upper()       
# set_list = list(set(alpa))    
# al_arr = []

# for i in set_list:
#     al_arr.append(alpa.count(i))   

# if  al_arr.count(max(al_arr)) > 1:    
#     print("?")
# else:
#     print(set_list[al_arr.index(max(al_arr))])

# print(set_list)
# print(al_arr,max(al_arr))
# print(al_arr.count(max(al_arr)))
# print(al_arr.index(max(al_arr)))

# 1152
# string_list = input().split()
# print(len(string_list))

# 2908
# sang = list(input().split())
# sang_arr = []
# for i in range(len(sang)):
#     sang_re = sang[i][::-1]
#     sang_arr.append(sang_re)
# print(max(sang_arr))

# su,sang = input().split()
# su = int(su[::-1])
# sang = int(sang[::-1])
# print(max(su,sang))

# 5622
# distr = input()

# dial = {2: ['A','B','C'], 3: ['D','E','F'], 4: ['G','H','I'], 5: ['J','K','L'], 6: ['M','N','O'], 7: ['P','Q','R','S'], 8: ['T','U','V'], 9: ['W','X','Y','Z']}

# cnt = 0

# dial_list = list(dial.values())
# dial_key = list(dial.keys())
# dial_items = (dial.items())

# for i in distr:
#     if i in dial_list[0]:
#         cnt += 3
#     elif i in dial_list[1]:
#         cnt += 4
#     elif i in dial_list[2]:
#         cnt += 5
#     elif i in dial_list[3]:
#         cnt += 6
#     elif i in dial_list[4]:
#         cnt += 7
#     elif i in dial_list[5]:
#         cnt += 8
#     elif i in dial_list[6]:
#         cnt += 9
#     elif i in dial_list[7]:
#         cnt += 10

# print(cnt)

# for i in distr:
#     for j,k in dial_items:
#         if i in k:
#             cnt += j+1

# print(cnt)


# 2941
# croatia = input()
# alpabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# for i in alpabet:
#     if i in croatia:
#         croatia = croatia.replace(i,"A")

# print(len(croatia),croatia)

# 1316

# word = int(input())
# cnt = word

# for i in range(word):
#     words = input()
#     for j in range(len(words)-1):
#         if words[j] == words[j+1]:
#             print(j,words[j])
#             continue
#         elif words[j] in words[j+1:]:
#             print(words[j+1:])
#             cnt-=1
#             break
        
# print(cnt)

# word1 = int(input())
# cnt1 = 0

# for i in range(word1):
#     words = input()
#     for j in range(0,len(words)-1):
#         if words[j] != words[j+1]:
#             gropu = words[j+1:]
#             if words[j] in gropu:
#                 cnt1-=1
#                 break
#     cnt1+=1

# print(cnt1)

# word2 = int(input())
# cnt2 = 0

# for i in range(word2):
#     words = input()
#     cnt = 0
#     for j in range(0,len(words)-1):
#         if words[j] != words[j+1]:
#             gropu = words[j+1:]
#             if gropu.count(words[j]) > 0:
#                 cnt += 1
#     if cnt == 0:
#         cnt2 += 1

# print(cnt2)
        
        

























