def solution(s):
    answer=[]
    s=s.split(" ")
    
    for words in s:
        #words[i]=words[i].capitalize()
        if words:
	        answer.append(words[0].upper()+words[1:].lower())
        else:
            answer.append(words)
    answer=" ".join(answer)
    
    return answer