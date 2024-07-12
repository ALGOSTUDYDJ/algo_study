# 백준 2166. 다각형의 면적

import sys
from collections import deque

# 다각형을 이루는 점이 순서대로 주어졌을 때,
# 선분 아래의 사다리꼴 면적을 더하고, 빼고를 교차한다.
# - 선분을 왼쪽으로 이을 때 더해줬으면, 오른쪽으로 이을 때는 빼준다.
# 선분이 N 개 생겨야하므로 2 번째 입력부터 N번째 입력까지에 대해서 선분을 이으며 진행해주고,
# 마지막 입력 이후에 처음 시작 선분과 이어주며 마지막 연산을 잇는다.
# 최종적으로 절대값을 취하고, 소숫점 둘 째 점에서 반올림한 값을 출력해준다.

N = int(input())

start = tuple(map(int, sys.stdin.readline().split()))

dq = deque([start])

area = 0

# N-1 번 입력
for _ in range(1, N):
    # 점 입력
    point = tuple(map(int, sys.stdin.readline().split()))
    dq.append(point)

    # 사다리꼴의 넓이 계산값을 면적에 더해주고
    quad = (dq[0][1] + dq[1][1] + 200000) * (dq[0][0] - dq[1][0]) / 2
    area += quad

    # 왼쪽 점을 빼줌
    dq.popleft()

quad = (dq[0][1] + start[1] + 200000) * (dq[0][0] - start[0]) / 2
area += quad

# 양식에 맞춰 반올림하기
area = abs(area)
print(area)
