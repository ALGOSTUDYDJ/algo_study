import sys

N, M = map(int, sys.stdin.readline().strip().split())

# 딕셔너리
pwd_dict = {}

# 비밀번호를 입력
for _ in range(N):
    site, pwd = sys.stdin.readline().strip().split()
    pwd_dict[site] = pwd

# 비밀번호를 출력
for _ in range(M):
    site = sys.stdin.readline().strip()
    print(pwd_dict[site])
