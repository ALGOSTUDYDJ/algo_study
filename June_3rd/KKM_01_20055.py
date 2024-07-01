def belt_answer(N, K, A):
    from collections import deque
    
    # 초기화
    belt = deque(A) # 덱 : 벨트 내구도 저장, 덱을 사용하면 회전을 쉽게 할 수 있음
    robots = deque([False] * N) # 로봇의 위치를 나타내는 덱, 초기에는 로봇이 없음
    step = 0 # 단계 수 초기화

    while True:
        step += 1 # 단계 수 증가
        
        # 1. 벨트가 회전한다.
        belt.rotate(1) # 벨트를 한 칸 회전
        robots.rotate(1)  # 로봇도 한 칸 회전
        robots[-1] = False  # 내리는 위치에 있는 로봇은 바로 내린다.
        
        # 2. 가장 먼저 벨트에 올라간 로봇부터 한 칸 이동할 수 있으면 이동한다.
        for i in range(N-2, -1, -1):  # 로봇을 뒤에서부터 검사

             # 다음 칸으로 이동 가능하면
            if robots[i] and not robots[i + 1] and belt[i + 1] > 0:
                robots[i] = False # 현재 위치에서 로봇 이동
                robots[i + 1] = True # 다음 위치로 로봇 이동
                belt[i + 1] -= 1 # 이동한 칸의 내구도 감소
        robots[-1] = False  # 내리는 위치에 있는 로봇은 내린다.
        
        # 3. 올리는 위치에 로봇을 올린다.

        # 올리는 위치의 내구도가 0이 아니면
        if belt[0] > 0:
            robots[0] = True # 로봇을 올리는 위치에 올림
            belt[0] -= 1   # 내구도 줄이기 
        
        # 4. 내구도가 0인 칸의 개수를 세기 

        # K개 이상이면 종료함
        if belt.count(0) >= K:
            break
    
    return step # 답 : 단계수


# 입력 받기
N, K = map(int, input().split())
A = list(map(int, input().split()))

result = belt_answer(N, K, A)

print(result)
