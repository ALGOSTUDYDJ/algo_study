- 투 포인터 문제 탕후루 문제입니다
N = int(input())
fruits = list(map(int, input().split()))

# 두 포인터를 초기화합니다.
left = 0
right = 0

#  딕셔너리
fruit_dict = {}

# 최대 길이
max_length = 0

# 오른쪽 포인터를 이동
while right < N:
    # 오른쪽 포인터의 과일을 추가합니다.
    if fruits[right] in fruit_dict:
        fruit_dict[fruits[right]] += 1
    else:
        fruit_dict[fruits[right]] = 1
    right += 1
    
    # 과일의 종류가 2개를 초과하는 경우 축소.
    while len(fruit_dict) > 2:
        fruit_dict[fruits[left]] -= 1
        if fruit_dict[fruits[left]] == 0:
            del fruit_dict[fruits[left]]
        left += 1
    
    # 최대 길이
    max_length = max(max_length, right - left)

print(max_length)