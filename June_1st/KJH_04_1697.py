# 백준 1697. 숨바꼭질

# 문제
# 수빈이는 동생과 숨바꼭질을 하고 있다.
# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
#
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
#
# 출력
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

from collections import deque

# 입력. N = 현재 위치 / K = 동생 위치
N, K = map(int, input().split())

# 방문처리 배열
visited = [False] * 200001

# deque을 활용한 풀이
q = deque([(0, N)])
visited[N] = True

# 결과값을 저장할 변수
target_cnt = 0

if N == K:
    print(0)
else:
    while q:
        cur = q.popleft()

        next_cnt = cur[0] + 1
        next_nums = cur[1] - 1, cur[1] + 1, cur[1] * 2

        for next_num in next_nums:

            if next_num == K:
                target_cnt = next_cnt
                break

            # 숫자가 0보다 작거나, 100,000 보다 크면 다음 반복
            if 0 <= next_num <= 100000 and not visited[next_num]:
                visited[next_num] = True
                q.append((next_cnt, next_num))

        # 만약 결과값인 target_cnt에 값이 저장됐으면 해당값 출력 후 반복문 종료
        if target_cnt:
            print(target_cnt)
            break