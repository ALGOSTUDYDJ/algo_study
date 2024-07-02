# 백준 1389. 케빈 베이컨의 6단계 법칙
# 그래프, BFS로 풀이
from collections import deque

# 사람 a, b가 주어졌을 때 케빈베이컨 수를 구하는 함수
def kevin_bacon(user):
    # distances 리스트는 현재 user로부터 인덱스 까지의 거리
    distances = [-1] * (N+1)
    distances[user] = 0
    q = deque([user])

    while q:
        cur = q.popleft()

        # 현재 친구를 맺은 관계들 중에서
        for friend in relations[cur]:
            # 만약 방문한 적이 없는 친구면,
            if distances[friend] == -1:
                # 거리 리스트에 현재 거리의 1을 더한 값을 저장
                distances[friend] = distances[cur] + 1
                # 저장하고 해당 친구를 q에 저장
                q.append(friend)

    # 거리의 합을 구할 때는 0번 값을 제외한 값들을 전부 더해줌
    sum_distance = sum(distances[1:])

    return sum_distance


# 유저 수 N, 친구 관계 수 M 입력
N, M = map(int, input().split())
min_kb = 10e9
min_kb_user = -1

# 모든 사람은 친구가 있음. 친구 관계는 방향이 없는 그래프 관계로 주어짐
relations = {i: set() for i in range(1, N+1)}

# A, B 관계를 입력받으며 해당 관계를 딕셔너리에 입력
for _ in range(M):
    A, B = map(int, input().split())
    relations[A].add(B)
    relations[B].add(A)

for i in range(1, N+1):
    # 유저 i 의 케빈 베이컨 수를 구함
    kb = kevin_bacon(i)

    # 현재 유저의 케빈 베이컨 수가 더 작으면, 해당 값으로 갱신
    if kb < min_kb:
        min_kb = kb
        min_kb_user = i

    elif kb == min_kb:
        if i < min_kb_user:
            min_kb_user = i

# 결과 출력
print(min_kb_user)