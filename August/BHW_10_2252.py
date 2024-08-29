# 2252. 줄 세우기

# 1. 위상 정렬을 이용한다.
# 2. 비교 시마다 키가 작은 학생에서 큰 학생으로 향하는 간선을 생성하고, 키가 큰 학생의 진입차수(비교 우위 횟수)를 1 증가한다.
# 3. 진입차수(비교 우위 횟수)가 0인 학생들을 큐에 삽입한다.
# 4. 큐를 순회하며 현재 순회 중인 학생보다 키가 큰 학생의 진입 차수(비교 우위 횟수)를 낮춘다.
# 5. 이 학생의 진입 차수가 0이 되면 큐에 삽입한다.
# 6. 큐가 빌 때까지 4-5를 반복한다.(큐가 빈다 = 모든 학생에 대해 정렬이 완료됐다.) 

import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # 학생의 수, 비교 횟수

graph = [[] for _ in range(N+1)]    # 그래프 생성
Degree = [0]*(N + 1)                # 진입차수(비교 우위 횟수) 배열 생성
q = []      # 큐
answer = [] # 정답 배열

# M개의 키 비교에 대해
for _ in range(M):
    A, B = map(int, input().split()) # 학생 A와 B
    graph[A].append(B)  # A에서 B로 향하는 간선 생성
    Degree[B] += 1      # B의 진입 차수 증가

# 키 정렬을 위해 진입차수가 0인 번호 탐색
for i in range(1, N+1):
    if Degree[i] == 0:
        q.append(i)

# 진입차수 순으로 키 정렬
while q:        # 모든 학생의 진입 차수가 0일 때까지
    new_q = []  # 새로운 큐 배열 생성
    for tmp in q:
        answer.append(tmp)  # 진입차수 낮은 순으로 삽입
        for j in graph[tmp]:# 해당 학생과 키 비교를 한 학생에 대해
            Degree[j] -= 1  # 차수를 낮춤
            if Degree[j]:   # 아직 키 작은 학생이 남아있으면 다음 학생 탐색
                continue
            new_q.append(j)
    q = new_q   # 큐 갱신

print(*answer)  # 출력