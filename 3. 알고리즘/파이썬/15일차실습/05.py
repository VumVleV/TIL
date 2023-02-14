# 방의 사이즈 입력
N = int(input())

# arr 선언
arr = [[0 for _ in range(N)] for _ in range(N)]

# arr에 행렬 받기
# i1은 행, i2는 열
for i1 in range(N):
    line_input = input()
    for i2 in range(N):
        arr[i1][i2] = line_input[i2]

# 누울 수 있는 자리 변수 지정
cnt_line = 0 #행으로
cnt_row = 0 #열로

# 스위치 변수
switch_box = 0

# 각 행에 연속한 두칸의 공간(.)이 존재하는지 확인하여 변수를 1만큼 증가시킨다
# 이 떄 박스에 의한 분할도 고려한다
for i3 in range(N):
    for i4 in range(N-1):   
        if switch_box == 0 and arr[i3][i4] == '.' and arr[i3][i4+1] == '.':
            cnt_line +=1
            switch_box = 1
        elif arr[i3][i4] == '.' and arr[i3][i4+1] == 'X':
            switch_box = 0
    switch_box = 0

# 열에 대해서도 확인한다
for i5 in range(N):
    for i6 in range(N-1):
        if switch_box == 0 and arr[i6][i5] == '.' and arr[i6+1][i5] == '.':
            cnt_row += 1
            switch_box= 1
        elif arr[i6][i5] == '.' and arr[i6+1][i5] == 'X':
            switch_box= 0
    switch_box = 0

# 요구 형식대로 출력
print(cnt_line, cnt_row)