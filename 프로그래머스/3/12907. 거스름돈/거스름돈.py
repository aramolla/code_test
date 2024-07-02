def solution(n, money):
    dp = [0] * (n+1)
    dp[0] = 1 # 0원을 만드는 경우의 수
    
    for coin in money: #1,2,5일때 1일경우 배열 업데이트 -> 2일 경우 배열
        for amount in range(coin, n+1):
            dp[amount] += dp[amount-coin] #배열 인덱스값 자체가 거스름돈 액수그렇게 때문에 2원 화폐의 경우의 수는 현재 자리에서 -2인덱스 자리에서 +1
            dp[amount] %= 1000000007 #정답 커질경우 대비(문제 제한 사항)
    return dp[n]