# 백준 27172. 수 나누기 게임
import sys

# 서로소 관계인지, 나누어떨어지는 값인지를 검사하는 게임
# 수가 1 ~ 1,000,000 까지이므로 인덱싱으로 수를 조회해야함
# 기본적으로 전부 검사하려면 O(N^2)로 플레이어 수만큼 검사하면 100,000이므로 반드시 시간초과

# 숫자를 전부 순회하며 해당 숫자의 배수 관계의 수가 있다면 전부 결과 승점 처리를 함
# 이 때, 배수가 배열에 확인됐는지 여부를 검사할 때 리스트보다 set이 훨씬 빠르므로,
# set으로 별도 저장해둔 뒤 확인하면 시간초과 해결 가능

N = int(input())
cnts = [0] * 1000001
card = list(map(int, input().split()))
card_set = set(card)

for i in card:
    for j in range(2 * i, 1000001, i):
        if j in card_set:
            cnts[i] += 1
            cnts[j] -= 1

for i in card:
    sys.stdout.write(str(cnts[i]) + ' ')