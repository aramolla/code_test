def solution(bandage, health, attacks):
    answer = 0
    idx=0
    pos=0
    temp=health #현재체력
    
    for i in range(1, attacks[-1][0]+1):
        
        if idx==len(attacks):
            break
        #몬스터 공격 시간
        if i == attacks[idx][0]:
            temp -= attacks[idx][1]
            if temp<=0:
                return -1
            idx+=1
            pos=0
        #기술 사용
        elif temp < health:
            temp += bandage[1]
            pos+=1
            if pos==bandage[0]:
                temp += bandage[2]
                pos=0
            temp=min(temp,health)
                    
    answer=temp
    return answer