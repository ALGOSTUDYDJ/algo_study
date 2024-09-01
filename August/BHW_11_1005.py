# 1005. ACM Craft

# 1. 위상 정렬을 이용
# 2. 건설 순서 순으로 간선을 연결
# 3. 진입 차수가 0인 건물들(바로 건설 가능한 건물들)을 현재 건설 큐에 삽입
#  삽입하면서 건설 소요 시간을 저장한다.
# 4. 큐를 순회하며 현재 건설 중인 건물 다음 순서의 건물에 진입 차수(건설 필요 건물 수)를 낮춘다
#  건설 소요 시간의 최댓값을 갱신한다.
# 5. 진입 차수(건설 필요 건물 수)가 0이 되면 다음 건설 큐에 삽입한다.
# 6. 4-5를 모든 건물을 건설할 때까지 반복한다.
# 7. 최종적으로 W에 해당하는 건물을 건설할 때까지의 소요 시간을 출력한다.

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())        # 건물의 수, 건설 순서 규칙
    graph = [[] for _ in range(N+1)]        # 그래프 생성
    Degree = [0]*(N + 1)                    # 진입차수(건설 순서) 배열 생성
    Ds = [0]
    Ds += list(map(int, input().split()))   # 건물 건설 소요 시간
    
    # 간선 연결 작업
    for _ in range(K):
        X, Y = map(int, input().split())    # 건설 순서
        graph[X].append(Y)                  # X에서 Y로 향하는 간선 생성
        Degree[Y] += 1                      # Y의 진입차수 생성
        
    DP = [0]*(N+1)  # 최소 건설 소요 시간 생성
    q = []          # 현재 건설 가능한 건물 배열
    
    # 진입 차수가 0인 건물들(바로 건설 가능한 건물들)을 현재 건설 큐에 삽입
    for i in range(1, N+1):
        if Degree[i]:
            continue
        DP[i] = Ds[i]   # 건설 소요시간 저장
        q.append(i)     # 건설 건물 삽입
    
    while q:
        next_q = []     # 다음 단계에 건설할 건물 배열
        # 큐를 순회하며 현재 건설 중인 건물 다음 순서의 건물에 진입 차수(건설 필요 건물 수)를 낮춘다.
        for now in q:
            # now 건물 다음으로 지을 수 있는 건물들을 순회하며
            for tmp in graph[now]:
                DP[tmp] = max(DP[tmp], Ds[tmp] + DP[now])   # 최소 건설 소요 시간 갱신
                Degree[tmp] -= 1    # 진입 차수 감소
                if Degree[tmp]:     # 아직 건물을 더 지어야 한다면 통과
                    continue
                next_q.append(tmp)  # 건설 시작이 가능하면 다음 순서에 건설
        q = next_q
        
    W = int(input())    # 백준이가 건설해야 할 번호
    print(DP[W])        # 건설 누적 소요 시간 출력