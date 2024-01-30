def solution(babbling):
    pos=0
    
    for word in babbling:
        list=["aya","ye","woo","ma"]
        current=''
        for s in word:
            current += s
            if current in list:
                list.remove(current)
                current=''
        if current=='':
            pos+=1
                
            
    return pos