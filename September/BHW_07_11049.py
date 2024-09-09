# 11049. 행렬 곱셈 순서

# 1. 행렬곱은 t점을 기준으로 왼쪽과 오른쪽으로 나눌 수 있다.
# 2. 왼쪽 묶음의 연산 횟수 DP[st][t], 오른쪽 묶음의 연산 횟수 DP[t + 1][st + term]
# 3. 왼쪽 묶음과 오른쪽 묶음을 연산하는 경우의 수 matrixs[st][0]*matrixs[t][1]*matrixs[st + term][1]
# 4. 2, 3을 끝까지 반복하며 각 경우의 최솟값을 갱신한다.
# 5. 시점 행렬과 종점 행렬까지 연산횟수의 최솟값을 출력한다. 

import sys
input = sys.stdin.readline

N = int(input())  # 행렬의 개수

matrixs = [list(map(int, input().split())) for _ in range(N)] # 행렬들

DP = [[0 for _ in range(N)] for _ in range(N)]  # 연산 수를 저장할 배열

# 구간의 길이마다 모두 계산
for term in range(1, N):
  # 가능한 모든 시점에서 구간의 길이까지의 연산 수를 구함
  for st in range(N):
    if st + term == N:
      break
    # 최초 충분히 큰 수로 초기화
    DP[st][st + term] = int(1e9)
    # 시점부터 종점까지 순회하며
    for t in range(st, st + term):
      # 연산 횟수는 시점부터 t까지의 연산 수 + t+1시점부터 종점까지의 연산 수 +
      # 시점 행렬의 행 수 * t 행렬의 열 수 * 종점 행렬의 열 수 와 기존 연산 수 중 최솟값(그렇게 합쳐졌기 때문)
      DP[st][st + term] = min(DP[st][st + term], 
                              DP[st][t] + DP[t + 1][st + term] + matrixs[st][0]*matrixs[t][1]*matrixs[st + term][1])

print(DP[0][-1])