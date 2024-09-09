# 1219. 오민식의 고민

# 1. 교통 수단 정보를 저장한다.
# 1-1. 최종 수입의 초깃값을 -inf로 설정하는 이유는 도착 도시까지의 수입이 음수일 수도 있기 때문이다.
# 2. 벨만-포드 알고리즘을 수행하여 양수 사이클 여부를 판별한다.
# 3. 양수 사이클이 발견되면 돈 복사가 가능하므로 gee를 출력한다.
# 4. 해당 도시까지 갈 수 있는 교통 수단이 없는 경우 gg를 출력한다.
# 5. 그 외의 경우에는 해당 도시까지의 비용을 출력한다.

import sys
input = sys.stdin.readline

N, S, E, M = map(int, input().split())  # 도시의 수, 시작 도시, 도착 도시, 교통 수단의 수
edges = []  # 교통수단 리스트
distance = [-sys.maxsize] * N           # 각 도시를 도착 도시로 했을 때 최종 수입

# 교통 수단 정보 저장
for _ in range(M):
    st, ed, w = map(int, input().split())
    edges.append((st, ed, w))           # 출발 도시, 도착 도시, 가격

# 오민식이 각 도시에서 벌 수 있는 최댓값
moneys = list(map(int, input().split()))

# 벨만 포드 수행
distance[S] = moneys[S] # 출발 도시 초기화

# 양수 사이클이 전파되도록 충분히 큰 수로 반복
for i in range(N + 101):
    for st, ed, w in edges:
        if distance[st] == -sys.maxsize:    # 출발 도시가 미방문 도시이면
            continue
        elif distance[st] == sys.maxsize:   # 출발 도시가 양수 사이클에 연결되었다면
            distance[ed] = sys.maxsize      # 도착 도시도 양수 사이클
        # 돈을 더 벌 수 있는 경우
        # 이전에 고려한 도착 도시에서까지의 수입이
        # 시작 도시까지의 수입 + 도착 도시에서 벌어들이는 수입 - 해당 도시까지 가는데 드는 비용
        # 보다 작다면 값을 갱신
        elif distance[ed] < distance[st] + moneys[ed] - w:
            distance[ed] = distance[st] + moneys[ed] - w
            # N - 1번 해도 값이 갱신된다는 것은(사이클이 생겼다)
            # 돈 복사가 가능하다
            if i >= N - 1:
                distance[ed] = sys.maxsize

# 도착하는 것이 불가능하다면(미방문)
if distance[E] == -sys.maxsize:
    print('gg')
# 양수 사이클이 있어 무한대로 돈을 벌 수 있다면
elif distance[E] == sys.maxsize:
    print('Gee')
# 양수 사이클 없으나 도착하는 경우 -> 최댓값
else:
    print(distance[E])