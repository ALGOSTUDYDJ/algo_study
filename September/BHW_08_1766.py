# 1766. 문제집

# 1. 위상 정렬과 우선순위 큐를 이용한다.
# 2. 차수를 문제 풀이에 필요한 문제 수로 정의한다
# 3. 차수가 0인 문제들을 우선순위 큐에 삽입한다.
# 4. 우선순위 큐에 문제들을 하나씩 빼면서 해당 문제를 풀이한다.
# 5. 해당 문제를 품으로써 제한을 하나씩 감소시킨다.
# 6. 차수가 0이 되면 우선순위 큐에 삽입한다.
# 7. 우선순위 큐가 빌 때까지 4-6을 반복한다.
# 8. 최종 풀이 순서를 출력한다.

import sys 
import heapq
input = sys.stdin.readline
N, M = map(int, input().split()) # 문제의 수, 정보의 수

# 가능한 쉬운 문제부터 풀어야 한다
degree = [0]*(N + 1)              # 어려운 문제를 풀기 위해 풀어야 하는 문제 수
graph = [[] for _ in range(N + 1)]
answer = []     # 문제 풀이
hq = []         # 문제 우선순위 큐

for _ in range(M):
  easy, hard = map(int, input().split())
  degree[hard] += 1         # 어려운 문제를 풀기 위해 먼저 풀어야 할 문제 수 증가
  graph[easy].append(hard)  # 문제 연결

# 문제 풀이에 제약이 없는 문항들 먼저 풀기(난이도 순)
for i in range(1, N + 1):
  if degree[i] == 0:
    heapq.heappush(hq, i)

# 다음 문제 풀이 
while hq:
  now = heapq.heappop(hq) # 먼저 풀 수 있는 순서대로
  answer.append(now)      # 문제풀이 진행
  for tmp in graph[now]:  # 이 문제를 품으로써 다음 문제 진행
    degree[tmp] -= 1      # 문제 풀이 제한 수 1 감소
    if degree[tmp]:
      continue
    heapq.heappush(hq, tmp) # 문제 풀이 가능 시 우선순위 큐에 삽입

print(*answer)  # 출력
