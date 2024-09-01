# 2623. 음악 프로그램

# 1. 위상 정렬을 이용한다.
# 2. 위상 정렬에서 진입 차수를 해당 가수의 최소 대기 가수 수로 생각한다.
# 3. 보조 PD들이 짜온 순서를 가지고 이전 가수와 다음 가수의 관계를 생성한다.
# 4. 진입 차수가 0(공연에 제약이 없는 가수들)인 가수들 부터 출연시킨다.
# 5. 출연 큐를 순회하며 현재 출연한 가수의 다음 순서 가수의 진입 차수를 1 낮춘다.
# 6. 다음 순서 가수의 진입 차수가 0이 되면 출연시킨다.
# 7. 5-6의 과정을 모든 가수가 출연할 때까지 반복시킨다.
# 8. 만약 진입 차수를 더 이상 줄일 수 없다면 순서를 짤 수 없다.(0 출력)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # 가수의 수, 보조 PD의 수
graph = [[] for _ in range(N + 1)]  # 그래프
Degree = [0]*(N+1)                  # 진입 차수(최소 대기 가수 수)

# 각 PD들이 정해온 순서 입력
for _ in range(M):
    num, prev, *singers = map(int, input().split()) # 인원과 출연 순서
    for singer in singers:
        graph[prev].append(singer)  # 이전 가수에서 다음 가수로 연결
        prev = singer               # 이전 가수 변경
        Degree[singer] += 1         # 대기 가수 수 증가

performed = [0]*(N + 1) # 공연 여부
performed[0] = 1
q = []                  # 큐시트  
# 순서에 제약이 없는 가수들(진입 차수가 0)부터 출연 대기
for i in range(1, N + 1):
    if Degree[i]:
        continue
    q.append(i)         # 큐시트에 추가
    performed[i] = 1    # 공연 여부 갱신

orders = q              # 공연 순서

while q:
    next_q = []         # 다음 공연 가능 가수 배열
    for now in q:
        for next in graph[now]: # 이 가수 다음 순서의 가수들을 순회
            Degree[next] -= 1
            if Degree[next]:    # 아직 다음 순서의 가수가 기다릴 가수가 남았다면 통과
                continue
            next_q.append(next) # 없다면 공연 진행
            performed[next] = 1 # 공연 여부 갱신
    
    q = next_q
    orders += next_q

# 모두 출연 가능한 경우에 출연 순서를 출력
if all(performed):
    for singer in orders:
        sys.stdout.write(f'{singer}\n')
else:
    print(0)    # 불가능한 경우 0을 출력