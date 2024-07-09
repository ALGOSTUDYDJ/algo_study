from collections import deque # 최소한의 이동횟수 : BFS 탐색

a, b, n, m = map(int, input().split())
stone = [-1]*100001
# -1 : 방문하지 않은 상태
# 0 또는 자연수 : 돌까지 점프한 횟수

def jumpcnt(start):
    q = deque()
    q.append(start)
    # 방문처리 -1 -> 0 
    stone[start] = 0

    while q:
        k = q.popleft()
        # 가능한 점프의 경우의 수 8개
        jumps = [k+1, k-1, k+a, k-a, k+b, k-b, k*a, k*b]
        for jump in jumps:
            # 범위 내부에 있어야하면서
            # 방문하지 않은 곳( = -1)만 다시 가야한다 (중복 방지)
            if 0<=jump<=100000 and stone[jump] == -1 :
                # 조건을 만족한다면
                # 새로운 도달점을 큐에 append 하고
                # 점프 횟수는 직전 것에 +1 계산해서 갱신한다.  
                q.append(jump)
                stone[jump] = stone[k] + 1
            

            if jump == m :
                return stone[jump]
    return stone[m]


print(jumpcnt(n))
