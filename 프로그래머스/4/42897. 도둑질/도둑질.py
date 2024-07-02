def solution(money):
    def rob(money):
        if len(money) == 0: #아래 케이스 나눈것때문
            return 0
        if len(money) == 1:
            return money[0]
        dp = [0]*(len(money))
        
        dp[0] = money[0] #
        dp[1] = max(money[0],money[1]) #인접하면 안되기때문에 0,1은 둘 중 큰 값 선택

        for i in range(2,len(money)):
            dp[i] = max(dp[i-1], dp[i-2]+money[i])
        
        return dp[-1]

    case1 = rob(money[:-1]) #첫번째 집을 터는 경우 마지막 집 터는 경우 제외하고 계산 시작
    case2 = rob(money[1:]) # 두번째 집을 터는 경우 첫번째 집을 터는 경우 제외하고 계산 시작
    
    return max(case1, case2)