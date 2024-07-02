# 1715. 카드 정렬하기


# 1. 두 묶음을 비교할 때 두 묶음의 카드 수의 합만큼 비교횟수가 증가한다.
# 2. 따라서 카드의 수가 적은 묶음부터 비교하면서 가장 숫자가 많은 묶음이 나중에 비교되어야 한다.
# 3. 우선순위 큐를 이용하여 카드의 수가 적은 두 묶음을 비교하여 합치면서 한 묶음으로 만들어 간다.

import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())
pq = PriorityQueue()

# 우선순위 큐에 값을 넣는다
for _ in range(N):
    pq.put(int(sys.stdin.readline()))

compares = 0                # 카드 비교횟수 

while pq.qsize() != 1:      # 비교할 카드 묶음이 없을 때까지
    low1 = pq.get()         # 카드 수가 가장 적은 묶음
    low2 = pq.get()         # 그 다음으로 적은 묶음
    compares += low1+low2   # 두 묶음의 비교횟수 증가
    pq.put(low1+low2)       # 두 묶음이 한 묶음이 되어 pq에 추가

print(compares)