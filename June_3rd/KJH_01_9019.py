# 백준 9019. DSLR
from collections import deque


# 테스트케이스 수 입력
T = int(input())

for tc in range(1, T+1):
    start, end = map(int, input().split())

    q = deque([(start, '')])
    visited = [False] * 10000
    visited[start] = True

    while q:
        cur, operands = q.popleft()

        # 만약 현재 값이 목표값과 동일해졌다면, 연산자(명령어)를 출력하고 반복 종료
        if cur == end:
            print(operands)
            break


        # 최종 명령어가 D S L R인 경우 각각에 대해 반복하며 다음 수를 구하고, end가 만들어지지 않은 경우 다음 수를 저장
        # D일 때, 2로 곱한 값의 일 ~ 천의 자릿수까지 남기고 레지스터에 저장
        next = (cur * 2) % 10000
        # 레지스터가 이미 방문한 숫자가 아니면 방문 처리 후 명령어에 D를 더해줌
        if not visited[next]:
            visited[next] = True
            q.append((next, operands + 'D'))

        # 1을 뺀 숫자 레즈스터리에 저장
        next = cur -1 if cur else 9999
        # 레지스터가 이미 방문한 숫자가 아니면 방문 처리 후 명령어에 S를 더해줌
        if not visited[next]:
            visited[next] = True
            q.append((next, operands + 'S'))

        # L, R에 해당하는 경우도 마찬가지로 수행
        next = (cur % 1000) * 10 + cur // 1000
        if not visited[next]:
            visited[next] = True
            q.append((next, operands + 'L'))

        next = (cur % 10) * 1000 + cur // 10
        if not visited[next]:
            visited[next] = True
            q.append((next, operands + 'R'))