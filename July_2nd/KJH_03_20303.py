# 백준 20303. 할로윈의 양아치
import sys
from collections import defaultdict


# 풀이 순서
# 아이들의 친구 관계를 파악해서 집합을 만든다. (사탕 수, 아이들 수) -> dfs
# 집합을 조합해서 아이들 수가 K 미만이 되고 사탕 수가 최대가 되는 조합을 만들고, 해당 사탕 수를 출력
# 집합을 만들고, 해당 집합의 아이들 수와 사탕 수의 배열에 추가
def dfs(start_child):
    global visited, cnts

    # 최종적으로 추가할 사탕 수의 합과 아이들 수를 0으로 초기화
    temp_sum = 0
    temp_cnt = 0

    # BFS 수행
    q = [start_child]
    while q:
        cur = q.pop()

        if visited[cur]:
            continue

        visited[cur] = True
        temp_sum += candies[cur - 1]
        temp_cnt += 1

        # 관계가 정의된 경우에 맺어진 관계를 순회하며 반복 수행
        if relations.get(cur):
            for next_child in relations[cur]:
                if not visited[next_child]:
                    q.append(next_child)

    # BFS 완료 후 서로소 집합의 (사탕 수, 아이들 수)를 배열에 저장
    cnts.append((temp_sum, temp_cnt))



# DP를 사용하여 최대 사탕 수를 찾습니다.
def knapsack():
    dp = [0] * K
    for candy, count in cnts:
        for i in range(K - 1, count - 1, -1):
            dp[i] = max(dp[i], dp[i - count] + candy)
    return max(dp)



# 입력 N: 아이들 수, M: 아이들 친구 관계 수, K: 넘지 말아야 할 아이들 수
N, M, K = map(int, sys.stdin.readline().split())
candies = list(map(int, sys.stdin.readline().split()))

# 아이들의 관계를 defaultdict에 저장
relations = defaultdict(list)

for _ in range(M):
    child1, child2 = map(int, sys.stdin.readline().split())
    relations[child1].append(child2)
    relations[child2].append(child1)

# 결과를 저장할 배열 초기화
cnts = []

# 방문처리 배열
visited = [False] * (N + 1)

for i in range(1, N + 1):
    if visited[i]:
        continue
    dfs(i)

# Knapsack 알고리즘을 사용하여 최대 사탕 수를 구합니다.
max_candy = knapsack()
print(max_candy)
