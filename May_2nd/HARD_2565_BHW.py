# 2565 전깃줄


# 1. 전봇대 형태로 구현하기 위해 전봇대 A에 걸린 높이 기준으로 정렬한다.
# 2. 줄이 교차한다는 것은 전깃줄의 전봇대 B에 걸린 높이가 A에서 더 높이 걸린 줄보다
# 3. 낮아졌다는 것을 의미한다. 즉, 증가수열의 최대 길이가 곧 전깃줄이 교차하지 않는
# 4. 전선의 최대 개수를 의미한다. 
# 5. 전선의 개수 - 증가수열의 길이가 구하고자 하는 제거해야 할 전깃줄의 최소 개수이다.

import sys
lines = [0]*501
N = int(sys.stdin.readline())

DP = [1]*N

lines = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
lines.sort()

# 전봇대 A에 높이 걸린 전깃줄부터 확인하면서
for i in range(1, N):
    # 전봇대 A에 더 높이 걸린 전깃줄을 순회하며
    for j in range(i):
        # B에 걸린 높이보다 더 높게 걸려 있으면
        if lines[i][1] > lines[j][1]:
            # 해당 전깃줄까지 꼬이지 않은 전깃줄의 개수 + 1
            DP[i] = max(DP[i], DP[j]+1)

print(N-max(DP)) # 전체 전깃줄의 수에서 꼬이지 않는 최대 전깃줄의 수를 뺌