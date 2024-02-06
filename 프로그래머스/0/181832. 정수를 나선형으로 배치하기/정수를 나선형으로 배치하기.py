def solution(n):
    answer = [[0 for j in range(n)] for i in range(n)]
    i = 0
    j = 0
    x=[0,1,0,-1]
    y=[1,0,-1,0]
    num=1
    pos=0
    
    while num <= n*n:
        answer[i][j]=num
        num+=1
        
        next_x=i+x[pos]
        next_y=j+y[pos]
        if 0<=next_x<n and 0<=next_y<n and answer[next_x][next_y]==0:
            i=next_x
            j=next_y
        else:
            pos=(pos+1)%4
            i=i+x[pos]
            j=j+y[pos]

    return answer
