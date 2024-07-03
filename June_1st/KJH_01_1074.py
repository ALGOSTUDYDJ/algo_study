# 백준 1074. Z
# 배열을 전부 쓰는 문제가 아니라 시간 제한이 주어지고 해당 행/열 위치의 숫자만 찾는 문제
# 배열의 크기 2^N을 기준으로 배열을 정사각형 모양으로 계속 반씩 잘라나가며 위치를 확인해서 값을 더해나가주면서 풀이
# 최종 배열의 크기(길이)가 1일 때의 값을 출력


# 첫 줄의 입력 N, r, c
N, r, c = map(int, input().split())

# 크기가 2^N * 2^N인 배열 생성
list_size = 1 << N

# 결과값을 저장할 target 생성
target = 0
# while문으로 종료될때까지 반복함
while True:

    # 리스트 사이즈를 절반으로 줄이고
    list_size >>= 1

    # 사분면 조사 (좌상 0, 우상 1, 좌하 2, 우하 3)
    quad = 0
    if c >= list_size:
        quad += 1
        c -= list_size
    if r >= list_size:
        quad += 2
        r -= list_size

    target += quad * list_size ** 2

    if list_size == 1:
        break

# 최종 결과값 출력
print(target)