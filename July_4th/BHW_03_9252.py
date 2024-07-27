# 9252. LCS 2

# 1. LCS 방법을 이용한다. 각 경우의 수들을 순회하며
# 2. 두 문자열의 각 순서에 해당하는 문자가 같으면 이전 순서
# (각 문자열의 해당 순서 - 1)의 길이에서 + 1을
# 3. 다르면 첫 문자열의 이전 순서까지의 최장 공통 부분 수열 길이와
# 두 번째 문자열의 이전 순서까지의 최장 공통 부분 수열 길이 중 큰 값을 가져온다.
# 4. 마지막까지 순회한 값이 두 문자열의 최장 공통 부분 수열의 길이이다.
# 5. 다시 두 문자열을 뒤부터 순회하며 부분 수열의 길이가 큰 방향으로 순회하며 문자열을 얻는다.
# (길이가 길다. = 해당 문자열의 순서가 공통 부분 수열에 해당한다.)
# 6. 문자열을 뒤집고 그 길이와 함께 출력한다.

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
first = list(input().rstrip())   # 첫 번째 문자열
second = list(input().rstrip())  # 두 번째 문자열

# 최장 공통 부분 수열을 저장할 배열 작성
DP = [[0 for _ in range(len(second) + 1)] for _ in range(len(first) + 1)] 
string = []

# 최장 공통 부분 수열의 길이를 
for i in range(1, len(first) + 1):
  for j in range(1, len(second) + 1):
    # 두 문자가 같다면 부분 수열의 길이 증가
    if first[i - 1] == second[j - 1]:
      # 이전 길이 + 1
      DP[i][j] = DP[i-1][j-1] + 1
    else:
      # 다른 경우 이전까지 최장 공통 부분 수열의 길이를 가져옴
      DP[i][j] = max(DP[i-1][j], DP[i][j-1])

# LCS 함수
def getText(r, c):
  # 어느 하나라도 마지막 글자에 도달한 경우 종료
  if r == 0 or c == 0:
    return
  # 확인하고 있는 두 문자가 같으면 기록하고 각 문자열의 이전 문자를 확인
  if first[r-1] == second[c - 1]:
    string.append(first[r-1])
    getText(r - 1, c - 1)
  # 다르면
  else:
    # 이전 두 상태(첫 문자열의 앞 글자, 두 번째 문자열의 앞 글자)를
    # 비교하여 최장 공통 부분 수열의 길이가 긴 쪽으로 이동
    if DP[r-1][c] > DP[r][c-1]:
      getText(r-1, c)
    else:
      getText(r, c-1)

getText(len(first), len(second))

string = string[::-1] # 문자열 뒤집기
print(DP[-1][-1])     # 길이 출력
print(''.join(string))  # 문자열 출력