# 백준 11404. 플로이드
import sys

# 플로이드 - 워셜 알고리즘을 사용한 풀이
# 삼중 for문으로, 시간복잡도는 n**3, 도시가 최대 100개이므로 무난한 풀이
#

# 도시 개수 n, 버스 개수 m개 입력
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 최대값으로 floyd 리스트 초기화
floyd = [[float('inf')] * n for _ in range(n)]
# 자기 도시로 오는 길은 0으로 초기화
for i in range(n):
    floyd[i][i] = 0

# 버스 노선 최소값으로 입력
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if c < floyd[a-1][b-1]:
        floyd[a-1][b-1] = c

# 플로이드-워셜 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            # 현재 경로 거리와 k를 거친 경로의 거리를 비교했을 때 더 작은 값으로 갱신
            if floyd[i][j] > floyd[i][k] + floyd[k][j]:
                floyd[i][j] = floyd[i][k] + floyd[k][j]

for i in range(n):
    for j in range(n):
        if floyd[i][j] == float('inf'):
            floyd[i][j] = 0
        print(floyd[i][j], end=" ")
    print()
