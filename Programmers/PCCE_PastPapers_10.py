def solution(mats, park):
    y = len(park) # Y축
    x = len(park[0]) # X축

    dp = [[0]*x for _ in range(y)] # 프레임 만들기
    size = 0 # 가능한 최대 크기의 돗자리값 저장변수

    for i in range(y):
        for j in range(x):
            if park[i][j] == "-1": # 빈자리 일때
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min( # 주변이 막혀 있나 안막혀 있나 확인 후 증가
                        dp[i-1][j], # 위
                        dp[i][j-1], # 왼쪽
                        dp[i-1][j-1] # 대각선
                    ) + 1

                size = max(size, dp[i][j]) # 최댓값 구하기

    answer = -1
    for mat in mats:
        if mat <= size: # 최댓값과 가지고있는 매트사이즈 비교
            answer = max(answer, mat) # 최댓값 저장

    return answer