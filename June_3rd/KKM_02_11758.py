def answer(x1, y1, x2, y2, x3, y3):
    # 세 점 P1 P2 P3 에서 두 벡터 A B를 다음과 같이 
    
    # 벡터 A =P2−P1
    # 벡터 B =P3−P2 라고하면 

    # 외적
    cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
    
    if cross_product > 0: # 양수는 반시계 1
        return 1 
    elif cross_product < 0: # 음수는 시계 -1
        return -1  
    else:
        return 0  # 0이명 두벡터는같은직선에 놓여있음

# 입력 
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())


result = answer(x1, y1, x2, y2, x3, y3)

print(result)