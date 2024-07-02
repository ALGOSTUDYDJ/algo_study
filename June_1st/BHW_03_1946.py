# 1946. 신입 사원


# 1. 서류 전형 혹은 면접 결과를 기준으로 정렬합니다.(여기선 서류 기준)
# 2. 서류 전형 1등의 면접 전형 성적을 서류 전형 차점자의 면접 성적과 비교합니다.
# 3. 서류 전형 1등의 면접 성적이 차점자의 면접 성적보다 등수가 높다면 차점자는 채용할 수 없습니다.
# 4. 다음 차점자의 면접 성적과 비교합니다.
# 5. 차점자의 면접 등수가 높다면 차점자의 면접 성적을 기준으로 다음 차점자의 면접 성적과 비교합니다.
# 6. 해당 차점자는 채용 가능합니다.
# 7. 서류 전형 최하위 등수까지 이를 반복합니다.

import sys
# 테스트 케이스의 수
T = int(input())
for _ in range(T):
    N = int(input())
    results = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    results.sort()          # 서류 전형 결과를 기준으로 정렬
    interview = results[0][1]   # 비교 기준이 되는 면접 전형 성적
    cnt = 1
    # 서류 전형 성적대로 순회
    for i in range(1, N):
        # 서류 전형이 밀리는 지원자가 면접 전형도 밀리는 경우 미채용
        if interview < results[i][1]:
            continue
        cnt += 1
        # 비교 대상이 되는 면접 성적 변경
        interview = results[i][1]
    
    print(cnt)