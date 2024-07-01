# 1629. 곱셈


# 1. 다음의 나머지 분배 법칙을 이용한다
# (A*B) % C = (A%C) * (B%C) % C
# 2. 지수(B)를 계속 2로 나누어(분할정복하여) 나누어 떨어지지 않을 때까지(분할) 나머지를 계산한 후
# 3. 위의 나머지 분배 법칙을 이용해 분할한 나머지들을 이용해 분할 전 나머지를 계산한다.(병합)


A, B, C = map(int, input().split())

def solution(a, b, c):  # a : 밑, b : 지수, c : 나눌 수
    # b가 1이면(거듭제곱할 것이 없으면)
    # a를 c로 나눈 나머지를 반호나
    if b == 1: 
        return a % c
    # a**(b//2) % c 를 계산
    # (a**b) % c = (a**(b//2) % c) * (a**(b//2) % c) % c 
    # b가 2이상의 홀수인 경우 (a % c) 추가
    # k = (a**(b//2) % c) 
    k = solution(a, b//2, c)
    
    if b%2:
        return (k*k*(a%c)) % c
    else:
        return (k*k) % c

print(solution(A, B, C))