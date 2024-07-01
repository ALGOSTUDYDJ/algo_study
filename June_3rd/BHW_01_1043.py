# 1043. 거짓말


# 1. 진실을 아는 사람이 없는 경우 모든 파티에서 과장 가능
# 2. 그렇지 않은 경우 각 파티의 1번 멤버의 대표자로 파티에 참여한 다른 멤버의 대표자를 병합
# 3. 각 파티를 순회하며, 1번 멤버가 진실을 아는 멤버와 대표자가 같다면 해당 파티에서 거짓말 불가
# 4. 거짓말 할 수 있는 총 파티의 수 출력

# 대표자를 찾는 함수
def find(a):
    # 자신이 대표이면 반환
    if a == parent[a]:
        return a
    # 아니라면 대표를 찾는다
    else:
        parent[a] = find(parent[a])
        return parent[a]

# 두 노드의 대표를 합치는 함수
def union(a, b):
    a = find(a)
    b = find(b)
    # 두 노드의 대표가 다르다면 a 쪽으로 합침
    # 같다면 합칠 필요 없음
    if a != b:
        parent[b] = a

N, M = map(int, input().split())    # 사람의 수 N, 파티의 수 M

# 진실을 아는 사람의 수와 번호
known_truth = list(map(int, input().split()))
if known_truth[0] == 0:     # 진실을 아는 사람이 없으면 모든 파티에서 과장 가능
    for _ in range(M):
        party = list(map(int, input().split()))
        
    print(M)
    
else:                       # 진실을 아는 사람이 있으면 과장 불가
    possible = M            # 과장할 수 있는 파티의 수(초기 값은 전체 파티 수)
    K = known_truth.pop(0)  # 진실을 아는 사람의 수와 진실을 아는 사람 번호 분리
    parent = [i for i in range(N+1)]
    parties = [[] for _ in range(M)]    # M개의 파티
    
    for i in range(M):  # M개의 파티에 대해
        l, *members = map(int, input().split())     # 인원 수와 멤버
        
        for j in range(1, l):                       # 1번 멤버를 대표자로 그루핑
            union(members[0], members[j])
        parties[i] = members                        # 멤버 정보 저장
    
    for i in range(M):      # M개의 파티에 대해
        for j in range(K):  # 진실을 아는 K명과 대표자가 같으면 파티 참석 불가
            if find(parties[i][0]) == find(known_truth[j]):
                possible -= 1   # 참석 가능한 파티 수 감소
                break
        
    print(possible)         # 참석 가능 파티 수 출력