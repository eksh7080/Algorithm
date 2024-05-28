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


"""
[문제]
길이가 같은 두 문자열 str1과 str2가 주어집니다.

두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.

[예시]
"aaaaa"	"bbbbb"  ->	"ababababab"
"""

# 내풀이
def solution(str1, str2):
    
    str = ''
    
    for i in range(len(str1)):
        str += str1[i] + str2[i]
        
    return str

# 인상적인 풀이 zip -> 두개의 배열 리스트를 묶어주는 함수
def solution(str1, str2):
    return ''.join(i+j for i,j in zip(str1,str2))

"""
[문제]
정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.

[예시]
60	2	3	-> 1
55	10	5	-> 0
"""

# 내풀이
def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    else:
        return 0
    
# 베스트 풀이
# 심플 이즈 베스트 별 다를바 없다.
    return 1 if number%n==0 and number%m==0 else 0


"""
[문제]
양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 
n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.

[예시]
7 -> 16
10 -> 220
"""

# 내풀이
def solution(n):
    
    divided = 'even' if n % 2 == 0 else 'odd'
    sum = 0
    
    for i in range(n + 1):
        if divided == 'even' and i != 1:
            i = i if i % 2 == 0 else 0
            sum += i**2
        elif divided == 'odd':
            i = i if i % 2 == 1 else 0
            sum += i
            
    return sum
                

# 인상적인 풀이
# sum 사용 유무가 포인트인거 같다.
def solution(n):
    # 풀이 1 -> 홀짝 구분을 이렇게도 한다.
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])

    # 풀이 2 창의적임
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)


"""
[문제]
문자열에 따라 다음과 같이 두 수의 크기를 비교하려고 합니다.

두 수가 n과 m이라면
">", "=" : n >= m
"<", "=" : n <= m
">", "!" : n > m
"<", "!" : n < m
두 문자열 ineq와 eq가 주어집니다. ineq는 "<"와 ">"중 하나고, eq는 "="와 "!"중 하나입니다. 
그리고 두 정수 n과 m이 주어질 때, n과 m이 ineq와 eq의 조건에 맞으면 1을 아니면 0을 return하도록 solution 함수를 완성해주세요.

[예시]
"<"	"="	20	50	-> 1
">"	"!"	41	78	-> 0
"""

# 내풀이 - 정석 그 자체
def solution(ineq, eq, n, m):
    if ineq == ">" and eq == "=":
        return int(n >= m)
    elif ineq == "<" and eq == "=":
        return int(n <= m)
    elif ineq == "<" and eq == "!":
        return int(n < m) 
    elif ineq == ">" and eq == "!":
        return int(n > m)


# 베스트 풀이 - eval 이라는 함수에 대해 몰랐다.
# 파이썬에서 사용가능한 문자열에 대한 식을 모두 계산해준다고 한다.
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))


"""
[문제]
두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, 
flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.

[예시]
-4	7	true	-> 3
-4	7	false	-> -11
"""
# 내 풀이
# 이게 곧 베스트, 삼항 연산자 사용
def solution(a, b, flag):
    return a+b if flag else a-b 






