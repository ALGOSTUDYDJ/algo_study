# 11758. CCW


# 1. 벡터의 외적을 이용한 CCW 공식 적용
# CCW = (X1Y2 + X2Y3 + X3Y1) - (X2Y1 + X3Y2 + X1Y3)
# 2. CCW 값이 음수이면 시계, 양수이면 반시계, 0이면 일직선

X1, Y1 = map(int, input().split())
X2, Y2 = map(int, input().split())
X3, Y3 = map(int, input().split())

# CCW 적용
CCW = (X1*Y2 + X2*Y3 + X3*Y1) - (X2*Y1 + X3*Y2 + X1*Y3)

# CCW 값에 따라 선분의 방향 판단
if CCW > 0:
    print(1)
elif CCW == 0:
    print(0)
else:
    print(-1)