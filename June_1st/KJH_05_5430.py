# 5430. AC


# 문제
# 선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.
#
# 함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.
#
# 함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다.
#
# 배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.

# 테스트케이스 수 입력
T = int(input())

for _ in range(T):
    # p: 실행할 함수, n: 배열에 들어있는 수의 개수
    p = input()
    # R이 두 번 연속으로 있으면 의미가 없는 값이므로, 'RR' -> ''으로 변경
    p = p.replace('RR', '')

    n = int(input())
    # 입력과 동시에 양끝의 괄호를 제거
    input_x = input()[1:-1]
    # ','를 기준으로 split한 정수의 리스트를 x로 저장
    if n:
        x = list(map(int, input_x.split(',')))
    else:
        x = []

    # 앞에서 몇 번 떼는지 확인 -> front
    front = 0
    # 뒤에서 몇 번 떼는지 확인 -> rear
    rear = 0
    # 지금이 앞인지, 뒤인지 확인 (1이면 정방향, -1이면 역방향)
    direction = 1

    # p 문자열을 순회해서, R이면 방향을 반대 방향으로 바꾸어주고, D면 현재 방향에 +1을 해줌
    for func in p:
        if func == 'R':
            direction *= -1
        else:
            if direction == 1:
                front += 1
            else:
                rear += 1

    # front와 rear의 합이 n보다 크다면 문자을 뗄 떼 에러가 나므로, 에러를 출력
    if front + rear > n:
        print('error')
    # 에러가 아닌 경우에, 문자열 슬라이싱 후 최종 방향대로 리스트를 설정
    else:
        if rear:
            x = x[front: -rear][::direction]
        else:
            x = x[front:][::direction]

        # 결과 문자열을 저장하고
        result_string = ''
        # 최종 결과 리스트를 순회하며, 콤마 (',')로 구분된 문자열로 만들어줌
        for xi in x:
            result_string += str(xi) + ','

        # 최종 결과 문자열로 만들어준 뒤 출력
        result = '[' + result_string[:-1] + ']'
        print(result)