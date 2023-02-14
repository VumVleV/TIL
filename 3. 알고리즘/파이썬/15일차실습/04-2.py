# 정답이나, 코드길이가 지나치게 길고 산만
# c언어로 비슷하게 했을 때, 100ms이하이나 거의 600ms가 나왔다ㅠㅠ

a = int(input())
for i in range(a):
    # (행: 1 ≤ b, 열: 1<= c ≤ 100)
    b, c = map(int,input().split())
    d = [[1 for _ in range(c)] for _ in range(b+1)]
    for j in range(b):
        e = list(map(int,input().split()))
        for k in range(c):
            d[j][k] = e[k]
    cnt_5 = 0
    for m in range(c):
        f = []
        for n in range(b+1):
            f.append(d[n][m])
        # print(f"f는 현재 {f}입니다")
        # 스위치 상수 정의
        cnt_1 = 0
        cnt_2 = 0
        cnt_3 = 0
        cnt_4 = 0
        cnt_6 = 0
        z = 0
        # z name_error 피하기 위해 값 지정
        for o in range(len(f)):
            if f[o] == 1 and cnt_1 == 0:
                cnt_1 = 1
                z = o
                # print(f"z는 {z}입니다!")
            if f[len(f)-1-o] == 1 and cnt_2 == 0:
                cnt_2 = 1
                y1 = len(f)-1-o
                # print(f"y1은 {y1}입니다!")
                # print(f"p 인덱스는 {y1-1}부터 {z+1}까지 순회합니다")
                if y1 != z+1:
                    # 3번째 조건의 입력에서 y1과 z 값 차이가 1이면, 36번째에서 for문이 작동하지 않고,
                    # 1by1, value=1의 케이스에서 y2가 지정되지 않는다 -> 53번, 55번 등 y2에서 index_error
                    for p in range(y1-1,z,-1):
                        # 마지막원소에 1이 연속으로 있을 경우
                        if f[p] == 1 and cnt_3 == 0:
                            y2 = p
                            cnt_6 = 1
                            # print(f"y2은 {y2}, p입니다!")
                        # 마지막원소가 0인 경우 피벗값을 반환
                        elif f[p] == 0 and cnt_6 == 0:
                            cnt_3 = 1
                            y2 = y1
                            # print(f"y2은 {y2}, y1입니다!")
                        # 그 외에 브레이크로 탈출한다
                        else:
                            break
                else:
                    y2 = 0
        if y2-z >= 2:
            # print(f"q 인덱스는 {y2-1}부터 {z}까지 순회합니다")
            for q in range(y2-1,z-1,-1):
                if f[q] == 1:
                    # print(f"cnt_5에 {y2-q-cnt_4-1}만큼 더합니다")
                    # print(f"그리고 cnt_4는 1만큼 증가합니다")
                    cnt_5 += (y2-q-cnt_4-1)
                    cnt_4 += 1
                    # print(f"cnt_5는 현재 {cnt_5}입니다")
                    # print(f"cnt_4는 현재 {cnt_4}입니다")
                else:
                    pass
        else:
            pass
    print(cnt_5)
    