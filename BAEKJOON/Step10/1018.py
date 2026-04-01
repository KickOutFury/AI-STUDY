a , b = map(int,input().split())

board = []

for _ in range(a):
    board.append(input()) # board[x][y]로 특정칸 추적 가능하게 저장

result = []
for i in range(a - 7): # 조각의 시작행을 정하는 반복문 / -7은 8칸짜리를 만들어야 하니, 시작점이 너무 아래쪽이면 안되기 때문
    for j in range(b - 7): # 조각의 시작열을 정하는 반복문 / i, j는 검사할 8x8 체스판의 왼쪽 위 좌표
        w_start = 0 # 왼쪽 위가 W로 시작하는 체스판으로 만들 때 바꿔야 하는 칸 수
        b_start = 0 # 왼쪽 위가 B로 시작하는 체스판으로 만들 때 바꿔야 하는 칸 수
        for x in range(i, i + 8): # 현재 선택한 8X8 조각의 행을 하나씩 보는 반복문
            for y in range(j, j + 8): # 현재 선택한 8x8 조각의 열을 하나씩 보는 반복문
                if (x + y) % 2 == 0: # 짝수 칸 추적 / 이 칸이 짝수 위치인지 홀수 위치인지 구분하기 위한 조건문 ex) 0,0 짝수 0,1 홀수 1,0 홀수 1,1 짝수 / 같은 색이어야 하는 칸들 구분용
                    if board[x][y] != 'W': # 같은 짝수 칸이지만, W로 시작하는 체스판이면 이 칸은 W여야함 근데 아니라면 바꿔줘야 하니 w_start + 1
                        w_start += 1 # w_start: W 시작 체스판으로 만들때 필요한 수정 수
                    if board[x][y] != 'B': # 같은 짝수 칸이지만, B로 시작하는 체스판이면 이 칸은 B여야함 근데 아니라면 바꿔줘야 하니 b_start + 1
                        b_start += 1 # b_start: B 시작 체스판으로 만들때 필요한 수정 수
                else: # 홀수 칸 추적 / 짝수 칸과 달리 홀수 칸은 짝수 칸과 반대색이 와야함
                    if board[x][y] != 'B': # 홀수 칸이 B면 W가 시작칸인데 B가 아니라면 바꿔줘야 하니 w_start + 1
                        w_start += 1
                    if board[x][y] != 'W': # 홀수 칸이 W면 B가 시작칸인데 W가 아니라면 바꿔줘야 하니 b_start + 1
                        b_start += 1
        result.append(min(w_start, b_start)) # 8x8 조각 하나에서 w시작 b시작 중에 더 적게 칠하는 경우 선택 ex) 조각1: w= 10, b= 12 => 10저장 , 조각2: w=8, b=20 => 8저장, 조각3: w=15, b=14 => 14저장

print(min(result)) # 모든 조각 중에서 가장 적게 칠하는 경우 선택