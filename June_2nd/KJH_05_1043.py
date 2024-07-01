# 백준 1043. 거짓말
# find 함수 정의
def find_set(x):
    global people

    if people[x] == x:
        return x

    return find_set(people[x])



# union 함수 정의
def union_set(x, y):
    global people

    x, y = find_set(x), find_set(y)

    if x == y:
        return

    if x < y:
        people[y] = x
    else:
        people[x] = y

# N: 사람 수, M: 파티의 수
N, M = map(int, input().split())

# 거짓말을 알아채는 사람이 없는 파티를 저장할 배열
parties = []

# 모든 사람의 대표자를 표현할 리스트 생성 (find_set-union의 make set 개념)
# 대표자는 본인으로 설정
people = [int(i) for i in range(N+1)]
# 진실을 아는 사람들의 리스트 입력,
people_truth = list(map(int, input().split()))

# 0명이 아니면 맨 앞의 수를 잘라서 인덱싱
if people_truth != [0]:
    people_truth = people_truth[1:]
    # 인덱싱 후 진실을 아는 사람들끼리 union
    for i in range(len(people_truth) - 1):
        union_set(people_truth[i], people_truth[i+1])

# 파티를 입력받으면서, 각 파티의 사람들끼리 전부 union
for i in range(M):
    party = list(map(int, input().split()))[1:]
    parties.append(party)
    for j in range(len(party) - 1):
        union_set(party[j], party[j+1])

# 진실을 아는 사람 set(tree)의 루트를 구하고
root = find_set(people_truth[0])

# 결과 저장 변수
cnt = 0


for party in parties:
    for person in party:
        if find_set(person) == root:
            break
    else:
        cnt += 1

# print(people_truth)
print(cnt)