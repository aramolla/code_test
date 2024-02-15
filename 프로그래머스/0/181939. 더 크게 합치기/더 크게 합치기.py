def solution(a, b):
    if str(a)+str(b)>str(b)+str(a):
        answer=str(a)+str(b)
    else:
        answer=str(b)+str(a)
    return int(answer)