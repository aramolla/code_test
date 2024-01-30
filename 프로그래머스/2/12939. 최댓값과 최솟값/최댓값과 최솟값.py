def solution(s):
    answer = ''
    list=sorted([int(i) for i in s.split()])
    
    answer =str(list[0])+" "+str(list[-1])
    return answer