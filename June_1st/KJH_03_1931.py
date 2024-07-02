# 백준 1931. 회의실


# 첫째 줄에 회의실 수 N 입력
N = int(input())

# 2 ~ N+1 줄까지 각 회의 정보 입력 (시작 ~ 끝나는 시간)
meetings = []

# (시작 시간, 종료 시간)의 튜플로 구성된 리스트를 저장
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 오름차순 정렬함
meetings.sort()

# 시작 최소 시간은 0, 종료 최대 시간은 2^31 - 1
cnt = 0
cur = (0, 0)

# 모든 회의실을 순서대로 순회함
for meeting in meetings:
    # 현재 미팅과 동일한 시간에 진행되면 다음 반복으로 넘어감
    if meeting == cur:
        # 회의의 시작 시간과 종료 시간이 같은 경우 시작하자마자 끝나므로 +1
        if cur[0] == cur[1]:
            cnt += 1
        continue

    # 현재 회의와 시간이 겹치는데, 종료 시간이 현재 회의보다 이르면 해당 회의로 대신 선정함
    if meeting[0] >= cur[0] and meeting[1] < cur[1]:
        cur = meeting
        continue

    # 선택 회의 시작 시간이 현재 회의 종료 시간과 같거나 더 늦으면, 해당 회의로 선택함
    if meeting[0] >= cur[1]:
        cur = meeting
        cnt += 1

print(cnt)