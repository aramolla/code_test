def solution(n, lost, reserve):
    
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
    lost_set = set(lost) - set(reserve)  # 차집합
    reserve_set = set(reserve) - set(lost)
    
    answer = n - len(lost_set)
    
    for i in lost_set:
           
        if i-1 in reserve_set:
            answer += 1
            reserve_set.remove(i-1)

        elif i+1 in reserve_set:
            answer += 1
            reserve_set.remove(i+1)
                
    return answer