# 14891. 톱니바퀴


# 1. 돌리고자 하는 톱니와 맞닿은 좌우측 톱니의 날의 극성에 따라 연쇄적으로 회전한다.
# 2. 입력받은 톱니부터 좌우측으로 순서대로 톱니를 검사한다.
# 3. 맞닿은 톱니의 극성이 같다면 해당 방향의 톱니의 회전 여부는 더 이상 검사하지 않는다.
# 4. 모든 회전이 끝난 후 점수를 계산한다.

wheels = [list(map(int, input())) for _ in range(4)]

K = int(input())
for i in range(K):
    wheel, d = map(int, input().split())    # 회전하는 톱니와 방향
    rotate_list = [(wheel-1, d)]            # 회전시킬 톱니 배열(바퀴 번호, 방향)
    left_d = right_d = d                    # 회전 방향
    left_wheel = wheels[wheel-1][6]         # 비교할 좌측 날
    right_wheel = wheels[wheel-1][2]        # 비교할 우측 날
    left = wheel-2                          # 왼쪽 톱니 번호
    right = wheel                           # 우측 톱니 번호
    while left >= 0 or right < 4:           # 좌우측에 돌릴 톱니가 남아있을 때까지
        ch = 0                              # 회전이 일어나지 않은 경우는 탐색 종료
        if left >= 0:
            if left_wheel != wheels[left][2] :      # 둘의 극이 다른 경우
                rotate_list.append((left, -left_d)) # 반대방향으로 회전시킬 배열에 추가
                left_wheel = wheels[left][6]        # 다음 비교할 좌측 날 지정
                left -= 1       # 비교할 톱니 지정
                left_d *= -1    # 회전했다면 방향은 반대
                ch += 1         # 회전 수 증가
                
        if right < 4:           # 우측도 같은 방식으로 진행
            if right_wheel != wheels[right][6]:
                rotate_list.append((right, -right_d))
                right_wheel = wheels[right][2]
                right += 1
                right_d *= -1
                ch += 1
        if ch == 0:
            break
    
    # 회전 수행
    for r in rotate_list:
        if r[1] == 1:       # 시계방향인 경우
            wheels[r[0]] = [wheels[r[0]][-1]] + wheels[r[0]][:7]
        else:               # 반시계방향인 경우
            wheels[r[0]] = wheels[r[0]][1:] + [wheels[r[0]][0]]
    rotate_list = []

# 점수 계산
temp = 1                # 현재 톱니의 점수
score = 0               # 현재까지 점수 총합
for wheel in wheels:
    if wheel[0] == 1:   # S극인 경우
        score += temp
    temp *= 2           # 다음 톱니의 점수는 현재의 2배

print(score)