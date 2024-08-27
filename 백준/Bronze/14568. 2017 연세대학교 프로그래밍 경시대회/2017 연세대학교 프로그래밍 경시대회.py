candy = int(input()) # 총 사탕 수

answer = 0 
for A in range(0, candy+1):
    for B in range(0, candy+1):
        for C in range(0, candy+1):
            if A+B+C == candy: # A,B,C 합이 전체 사탕 개수
                if C >= B+2: # C가 B보다 2개 이상 많음
                    if A != 0 and B != 0 and C != 0: # A,B,C는 0x
                        if A % 2 == 0: # A는 짝수
                            answer += 1
print(answer)