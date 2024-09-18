# 11689. GCD(n, k) = 1

# 1. n과 서로소인 자연수 k의 수를 구하는 문제
# 2. 작은 수부터 탐색을 해서 n의 소인수를 찾는다.
# 3. n의 소인수 p를 찾은 경우 결과 경우의 수에서 p의 배수를 모두 제거한다.(n과 서로소가 아님)
# 4. 중복 계산을 방지하기 위해 n을 p로 나뉠때까지 나눠준다.
# 5. 최종 결과의 경우의 수를 출력한다.

import math
n = int(input())    # 입력 n
result = n          # 결과 수

for p in range(2, int(math.sqrt(n)) + 1):
    if n % p == 0:              # p가 n의 소인수라면
        result -= result // p   # p의 배수는 서로소가 아님
        while n % p == 0:       # 소인수 p를 모두 없앰
            n //= p

# 반복문에서 제곱근까지만 탐색했으므로 1개의 소인수가 누락되는 케이스 처리
if n > 1:
    result -= result // n

print(int(result))