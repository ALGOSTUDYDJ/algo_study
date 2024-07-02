# 백준 2458. 키 순서
import sys

# 키 순서를 유츄할 수 있는 사람의 수를 구하는 문제
# 플루이드-워셜 알고리즘을 응용
# 확실히 본인보다 작은 것을 알 수 있는 사람을 확인하는 배열과,
# 확실히 본인보다 큰 것을 알 수 있는 사람을 확인하는 배열을 두 개 만들고
# 플루이드-워셜 알고리즘으로 경로를 찾을 수 있는 경우를 1(True)로 설정
# 크거나 작은 배열(사람 수)의 총합이 N-1이 넘는 경우만 계산해서 답 출력

# N, M 입력
N, M = map(int, sys.stdin.readline().split())
# 작은 사람들을  찾는 리스트 smaller, 큰 bigger
smaller = [[0] * N for _ in range(N)]
bigger = [[0] * N for _ in range(N)]

# 두 이차원 리스트 전부에 입력을 받음
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    smaller[a-1][b-1] = 1
    bigger[b-1][a-1] = 1

# k -> i -> j를 순회하면서, 연쇄 가능한 모든 경우를 이어줌
for k in range(N):
    for i in range(N):
        for j in range(N):
            if smaller[i][k] and smaller[k][j]:
                smaller[i][j] = 1
            if bigger[i][k] and bigger[k][j]:
                bigger[i][j] = 1

result = 0

# 결과로 대소 유추가 가능한 사람의 수가 N-1이 넘는 경우를 추가
for i in range(N):
    if sum(smaller[i]) + sum(bigger[i]) >= N-1:
        result += 1

print(result)