
# 공유기간의 거리가 mid일 때 설치할 수 있는 공유기 수

# 거리를 이분탐색으로 찾는 과정이다.
# 입력값이 많아서 써줍니다.
import sys
input = sys.stdin.readline

# 입력 받기
n, c  = map(int, input().split())

# 집의 좌표들을 저장할 배열 생성
houses = []

# 집의 좌표를 입력받고 배열에 저장
for _ in range(n):
    house_location = int(input())
    houses.append(house_location)
houses.sort()

# 한 집에 하나의 공유기만 설치 가능하기 때문에
start = 1
# 각 끝에 있는 집 사이의 거리가 공유기 간 최대 거리이기 때문에
end = houses[-1] - houses[0]
# 결과
result = 0

# 이진 탐색 시작
while (start <= end):
    # 공유기 간의 거리 : mid
    mid = (start + end) // 2
    current = houses[0]
    count = 1
    
    # 공유기를 몇대 설치할 수 있는지 확인
    for i in range(1, len(houses)):
        if houses[i] >= current + mid:
            count += 1
            current = houses[i]
        
    if count >= c:
        start = mid + 1
        result = mid
    
    else:
        end = mid - 1
        
print(result)
