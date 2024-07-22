def solution(number, k):
    stack = []
    
    for num in number:
        while stack and k > 0 and num > stack[-1]:
            k -= 1 # 지울때마다 k줄임
            stack.pop() # 스텍에 있는거 지움
        stack.append(num) # 스텍에 추가
        
        
    if k > 0:
        stack = stack[:-k]
        
    answer = ''.join(stack)
        
    return answer