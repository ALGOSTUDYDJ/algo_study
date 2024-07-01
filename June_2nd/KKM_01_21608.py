N = int(input())
student_love = [list(map(int, input().split())) for _ in range(N**2)]

seat = [[0]*N for _ in range(N)]
love = {}  # 딕셔너리!

# 학생 : 좋아하는 4명 저장
for student in student_love:
    # 0번째 인덱스(학생) = 1: 이후 인덱스 (좋아하는사람 네명) 
    love[student[0]] = student[1:]


'''
print(love) 

{4: [2, 5, 1, 7],
 3: [1, 9, 4, 5],
 9: [8, 1, 2, 3],
 8: [1, 9, 3, 4],
 7: [2, 3, 4, 8],
 1: [9, 2, 5, 7],
 6: [5, 2, 3, 4],
 5: [1, 9, 2, 8],
 2: [9, 3, 1, 4]}
'''

# 방향 벡터 (상하좌우) |r1 - r2| + |c1 - c2| = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_seat(student):
    max_love = -1  # 인접 칸의 좋아하는 학생 수 (최댓값)
    max_empty = -1  # 인접 칸의 빈 자리 수 (최댓값)
    best_seat = (N, N)  # 최선의 자리를 저장할 변수

    for x in range(N):
        for y in range(N):
            if seat[x][y] == 0:  # 빈 자리
                love_cnt = 0 # 인접 칸의 좋아하는 학생 수
                empty_cnt = 0 # 인접 칸의 빈 자리 수

                # 방향 벡터
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:

                        # 좋아하는 학생 있으면 love 변수 +1
                        # 없고 빈자리면 empty 변수 +1
                        if seat[nx][ny] in love[student]:
                            love_cnt += 1
                        if seat[nx][ny] == 0:
                            empty_cnt += 1

               
               # 여기서부터 어려웠음

                # 튜플! (좋아하는 학생 수, 빈 칸 수, 행 음수, 열 음수)
                current = (love_cnt, empty_cnt, -x, -y)
                best = (max_love, max_empty, -best_seat[0] if best_seat != (N, N) else -1, -best_seat[1] if best_seat != (N, N) else -1)


                # 이렇게 하면 튜플의 첫번째 요소부터 비교함..
                if current > best:
                    best_seat = (x, y)
                    max_love = love_cnt
                    max_empty = empty_cnt
    
    return best_seat

# 자리 배치
for student in student_love:
    pos = find_seat(student[0])
    seat[pos[0]][pos[1]] = student[0]

# 만족도 계산
satisfaction = 0

for x in range(N):
    for y in range(N):
        student = seat[x][y]
        love_count = 0
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if seat[nx][ny] in love[student]:
                    love_count += 1


        # 문제 조건대로 만족도 계산함
        if love_count == 1:
            satisfaction += 1
        elif love_count == 2:
            satisfaction += 10
        elif love_count == 3:
            satisfaction += 100
        elif love_count == 4:
            satisfaction += 1000

print(satisfaction)

