# 2023. 신기한 소수


# 신기한 소수 : 왼쪽부터 모든 자릿수까지 소수인 수
# N 자리 신기한 소수 출력

# 1. 1자리 소수는 2, 3, 5, 7이므로 왼쪽 처음에 들어올 수 있는 수는 2, 3, 5, 7
# 2. 그 외 자릿수에 짝수가 들어오는 경우 소수가 아니므로 홀수만 매칭
# 3. 해당 수가 소수이면 다음 자릿수 탐색
# 4. 최종적으로 N자리까지 모두 소수인 경우 출력

import sys
sys.setrecursionlimit(10000)

N = int(input())    # 자릿수

# 소수 판별 함수
def isPrime(number):
    # 제곱근 이하의 수에서 나누어 떨어지면 소수가 아님
    for i in range(2, int(number**(1/2) + 1)):
        if number % i == 0:
            return False
    # 모두 나누어 떨어지지 않았으면 소수
    return True

# 신기한 소수를 생성하는 함수
def DFS(number):    # 입력으로 들어오는 소수
    # 종료조건 : N자릿수
    if len(str(number)) == N:
        print(number)
        return
    # 이외
    for i in range(1, 10, 2):   # 짝수가 들어간다면 소수가 아니므로 홀수만 확인
        # 소수인지 확인
        if isPrime(number*10 + i):
            DFS(number * 10 + i)    # 소수이면 자릿수를 늘림

# 1자리 소수는 2, 3, 5, 7이므로 
# 2, 3, 5, 7을 왼쪽 첫 자릿수로 하는 수만 탐색
DFS(2)
DFS(3)
DFS(5)
DFS(7)