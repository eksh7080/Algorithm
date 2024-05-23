"""
[문제]
더 크게 합치기

[설명]
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

12 ⊕ 3 = 123
3 ⊕ 12 = 312
양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.

단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.

[예시]
---
a	b	result
9	91	991
89	8	898
---
"""

def solution(a, b):
    a_sum = int(str(a)+str(b))
    b_sum = int(str(b)+str(a))
    
    if a_sum > b_sum:
        return a_sum
    elif a_sum < b_sum:
        return b_sum
    elif a_sum == b_sum:
        return a_sum
    
"""
[문제]
홀짝 구분하기

[설명]
자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.

[예시]
입력 #1 - 100
출력 #1 - 100 is even
"""

# 내 풀이
a = int(input())

if a % 2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')

# 베스트 풀이 미친풀이;;
n = int(input())
print(f"{n} is {'eovdedn'[n&1::2]}")


"""
[문제]
특수문자 출력하기

[설명]
다음과 같이 출력하도록 코드를 작성해 주세요.

[예시]
!@#$%^&*(\'"<>?:;
"""

# 내풀이
print('!@#$%^&*(\\\'"<>?:;')

# 베스트 풀이 
# r -> raw를 의미하며 regex 패턴에서 자주 사용함
print(r'!@#$%^&*(\'"<>?:;')

"""
[문제]
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

12 ⊕ 3 = 123
3 ⊕ 12 = 312
양의 정수 a와 b가 주어졌을 때, a ⊕ b와 2 * a * b 중 더 큰 값을 return하는 solution 함수를 완성해 주세요.

단, a ⊕ b와 2 * a * b가 같으면 a ⊕ b를 return 합니다.

[예시]
2	91	364
91	2	912
"""

# 내풀이
def solution(a, b):
    s1 = str(a)
    s2 = str(b)
    sum1 = int(s1+s2)
    sum2 = (2 * a * b)
    
    if sum1 > sum2:
        return sum1
    elif sum1 < sum2:
        return sum2
    else:
        return sum1

# 베스트 풀이  
# max의 인자값으로 해결 가능
    return max(int(str(a) + str(b)), 2 * a * b)

"""
[문제]
정수 num과 n이 매개 변수로 주어질 때, num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.

[예시]
98	2	1
34	3	0
"""

# 내풀이
def solution(num, n):
    return 1 if num % n == 0 else 0

# 베스트 풀이  
# not의 존재를 이제 알았다.
    return int(not(num % n))