# 백준 11286. 절대값 힙

# 배열에 절대값의 최소값을 기준으로 힙 정렬을 한다.
# 절대값의 최소값 기준으로 저장 및 출력을 위해서 힙에 (절대값, 실제값) 기준으로 저장해주고,
# heappop, heappush로 입출력을 제어해준다.
# 입출력은 표준 입출력을 사용해서 시간을 줄인다.

import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())
hq = []

for _ in range(N):
    cur = int(sys.stdin.readline())

    if not cur:
        if hq:
            sys.stdout.write(heappop(hq)[1] + '\n')
        else:
            sys.stdout.write('0' + '\n')
    else:
        heappush(hq, (abs(cur), cur))