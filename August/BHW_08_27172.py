# 27172. 수 나누기 게임

# 1. 각 카드 숫자 별 점수를 계산하기 위한 배열을 생성한다.
# 2. 각 카드(플레이어)를 순회하며 에라토스테네스의 체를 이용하여 카드의 배수를 찾는다.
# 3. 배수에 해당하는 숫자를 가진 상대 플레이어가 있으면 플레이어는 점수를 얻고 상대는 잃는다.
# 4. 플레이어에 해당하는 숫자대로 점수를 출력한다.

import sys
input = sys.stdin.readline

N = int(input())    # 플레이어의 수
cards = list(map(int, input().split())) # 카드

cards_with_idx = {card: idx for idx, card in enumerate(cards)}
max_card = max(cards)  # 최댓값
scores = [0 for _ in range(N)]    # 각 카드 숫자에 해당하는 점수 배열

# 각 카드를 순회하면서
for i in range(N):
    cur_card = cards[i]
    # 에라토스테네스의 체를 이용해 배수를 탐색
    for j in range(cur_card*2, max_card+1, cur_card): 
        # 해당 배수를 가진 플레이어가 존재하는 경우
        if j in cards_with_idx:
            idx = cards_with_idx[j] # 상대의 결과
            scores[i] += 1      # 플레이어는 점수를 얻음
            scores[idx] -= 1    # 상대는 점수를 잃음

print(*scores)