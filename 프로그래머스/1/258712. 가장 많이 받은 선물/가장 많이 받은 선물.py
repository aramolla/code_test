def solution(friends, gifts):
    answer = 0
    #주고받은표
    list = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    
    for i in range(len(gifts)):
        a=gifts[i].split()
        pos1=friends.index(a[0])
        pos2=friends.index(a[1])
        list[pos1][pos2]+=1
        
    #주고받은 수
    give = [0 for _ in range(len(friends))]
    send = [0 for _ in range(len(friends))]
    
    for i in range(len(friends)):
        give[i] = sum(list[i])
        for j in range(len(friends)):
            send[i] += list[j][i]
            
    #선물지수
    gift_score=[0] * len(friends)
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i!=j:
                gift_score[i] = give[i] - send[i]
    
    #받을 선물 수 예상
    gift_num = [0 for _ in range(len(friends))]
    
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i != j:
                if list[i][j]>list[j][i]:
                    gift_num[i]+=1
                elif list[i][j]==list[j][i]:
                    if gift_score[i]>gift_score[j]:
                        gift_num[i]+=1
                    
    answer=max(gift_num)
    
    return answer