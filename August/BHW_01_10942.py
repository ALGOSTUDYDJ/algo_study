# 10942. 팰린드롬

# 1. 팰린드롬의 조건
# - 길이가 1이면 팰린드롬
# - 길이가 2이면 두 수가 같으면 팰린드롬
# - 길이가 3 이상이면 양 끝 수가 같고 양 끝 수를 제외한 수열이 팰린드롬이면 팰린드롬
# 2. 길이가 1, 2인 경우의 팰린드롬 여부를 저장한다.
# 3. 길이가 3 이상인 경우부터 길이 N까지의 팰린드롬 여부를 저장한다.
# 4. 각 케이스에 대한 판별 결과를 출력한다.

import sys

input = sys.stdin.readline
N = int(input())  # 수열의 크기
nums = list(map(int, input().split())) # 수열
DP = [[0 for _ in range(N)] for _ in range(N)]  # DP 배열

# 수열의 길이가 1인 경우는 무조건 팰린드롬
for i in range(N):
  DP[i][i] = 1 

# 길이가 2인 경우는 두 수가 같으면 팰린드롬
for i in range(N-1):
  if nums[i] == nums[i + 1]:
    DP[i][i + 1] = 1

# 숫자가 3개 이상인 경우는 양 끝 숫자가 같고 그 사이 숫자가 팰린드롬이면 팰린드롬
for length in range(2, N):     # 수열의 길이(수 하나가 0, 수 3개는 2)
  for s in range(N - length):  # 시점의 위치
    e = s + length # 종점의 위치
    # 시점과 종점이 같고 그 사이 수열이 팰린드롬인 경우 팰린드롬
    if nums[s] == nums[e] and DP[s + 1][e - 1]:
      DP[s][e] = 1

# 팰린드롬 판별
M = int(input())
for _ in range(M):
  s, e = map(int, input().split())      # 시점, 종점
  sys.stdout.write(f'{DP[s-1][e-1]}\n') # 팰린드롬 판별